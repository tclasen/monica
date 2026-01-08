"""FFmpeg job executor with progress display."""

import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from colorama import Fore, Style

from .recipes import Recipe
from .logger import get_logger


def generate_output_filename(input_file: Path, recipe: Recipe, export_dir: Path) -> Path:
    """Generate the output filename based on naming convention.

    Format: <original_name>_<YYYYMMDD_HHMMSS>_<format>_converted.<ext>
    """
    original_name = input_file.stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    format_name = recipe.extension.lstrip(".").upper()

    output_name = f"{original_name}_{timestamp}_{format_name}_converted{recipe.extension}"
    return export_dir / output_name


def parse_duration(line: str) -> float | None:
    """Parse duration from FFmpeg output (in seconds)."""
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+)\.(\d+)", line)
    if match:
        hours, minutes, seconds, centiseconds = map(int, match.groups())
        return hours * 3600 + minutes * 60 + seconds + centiseconds / 100
    return None


def parse_time(line: str) -> float | None:
    """Parse current time from FFmpeg progress output (in seconds)."""
    match = re.search(r"time=(\d+):(\d+):(\d+)\.(\d+)", line)
    if match:
        hours, minutes, seconds, centiseconds = map(int, match.groups())
        return hours * 3600 + minutes * 60 + seconds + centiseconds / 100
    return None


def display_progress_bar(percent: float, width: int = 40) -> None:
    """Display a progress bar to stdout."""
    filled = int(width * percent / 100)
    bar = "=" * filled + "-" * (width - filled)
    print(f"\r[{bar}] {percent:5.1f}%", end="", flush=True)


def run_ffmpeg_job(
    ffmpeg_path: str,
    input_file: Path,
    output_file: Path,
    recipe: Recipe
) -> tuple[bool, str]:
    """Run a single FFmpeg job with progress display.

    Args:
        ffmpeg_path: Path to FFmpeg executable
        input_file: Input file path
        output_file: Output file path
        recipe: The recipe to apply

    Returns:
        Tuple of (success, error_message)
    """
    cmd = [
        ffmpeg_path,
        "-i", str(input_file),
        "-y",  # Overwrite output
        "-progress", "pipe:1",  # Progress to stdout
        "-nostats",
        *recipe.ffmpeg_args,
        str(output_file)
    ]

    logger = get_logger()
    logger.debug(f"Running command: {' '.join(cmd)}")

    try:
        # First, get the duration using ffprobe-style call
        duration_cmd = [
            ffmpeg_path,
            "-i", str(input_file),
            "-f", "null",
            "-"
        ]

        duration = None
        probe_result = subprocess.run(
            duration_cmd,
            capture_output=True,
            text=True,
            timeout=30
        )

        # Duration is in stderr
        for line in probe_result.stderr.split("\n"):
            duration = parse_duration(line)
            if duration:
                break

        # Run the actual conversion
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        current_time = 0

        # Read progress from stdout
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break

            if line.startswith("out_time="):
                # Parse time in format HH:MM:SS.microseconds
                time_str = line.strip().split("=")[1]
                match = re.match(r"(\d+):(\d+):(\d+)\.(\d+)", time_str)
                if match:
                    h, m, s, us = match.groups()
                    current_time = int(h) * 3600 + int(m) * 60 + int(s) + int(us) / 1000000

                    if duration and duration > 0:
                        percent = min(100, (current_time / duration) * 100)
                        display_progress_bar(percent)

            elif line.startswith("progress=end"):
                display_progress_bar(100)
                print()  # New line after progress bar
                break

        # Wait for process to complete
        process.wait(timeout=60)
        stderr = process.stderr.read()

        if process.returncode != 0:
            logger.error(f"FFmpeg failed: {stderr}")
            return False, stderr

        return True, ""

    except subprocess.TimeoutExpired:
        process.kill()
        return False, "Process timed out"
    except Exception as e:
        return False, str(e)


def execute_jobs(
    ffmpeg_path: str,
    files: list[Path],
    recipe: Recipe,
    export_dir: Path
) -> bool:
    """Execute a queue of FFmpeg jobs.

    Processes files one at a time. Stops immediately on error.

    Args:
        ffmpeg_path: Path to FFmpeg executable
        files: List of input files
        recipe: The recipe to apply
        export_dir: The export directory

    Returns:
        True if all jobs completed successfully, False otherwise
    """
    logger = get_logger()
    logger.job_start([str(f) for f in files], recipe.name)

    total = len(files)
    print(f"\n{Fore.CYAN}Processing {total} file(s) with '{recipe.name}'...{Style.RESET_ALL}")

    for i, input_file in enumerate(files, 1):
        output_file = generate_output_filename(input_file, recipe, export_dir)

        print(f"\n{Fore.CYAN}[{i}/{total}]{Style.RESET_ALL} {input_file.name}")
        print(f"    -> {output_file.name}")

        logger.item_start(input_file.name)

        success, error = run_ffmpeg_job(ffmpeg_path, input_file, output_file, recipe)

        if success:
            logger.item_end(input_file.name, True)
            print(f"{Fore.GREEN}Done!{Style.RESET_ALL}")
        else:
            logger.item_end(input_file.name, False)
            logger.error(f"Error processing {input_file.name}: {error}")

            print(f"\n{Fore.RED}Error:{Style.RESET_ALL} Failed to process {input_file.name}")
            print(f"{Fore.RED}Job stopped. See logs for details.{Style.RESET_ALL}")

            logger.job_end(False, recipe.name)
            return False

    logger.job_end(True, recipe.name)
    print(f"\n{Fore.GREEN}All {total} file(s) processed successfully!{Style.RESET_ALL}")
    return True
