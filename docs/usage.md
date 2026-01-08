# MONICA User Guide

This guide covers everything you need to know to use MONICA effectively.

## Getting Started

### First Run

When you run MONICA for the first time:

1. The application creates three folders:
   - `import/` - Place your input files here
   - `export/` - Converted files appear here
   - `logs/` - Application logs are stored here

2. MONICA checks for FFmpeg:
   - If found in your system PATH: Shows green "[OK]" status
   - If not found: Offers to download automatically

### Navigation

MONICA uses keyboard-only navigation:

| Key | Action |
|-----|--------|
| **Arrow Up/Down** | Move between menu items |
| **Enter** | Select/confirm |
| **Space** | Toggle selection (in file picker) |
| **Ctrl+C** | Exit/cancel |

## Main Menu Options

### Convert Video

Converts video files to different formats with re-encoding.

**Available presets:**
- MP4 (H.264) - Standard compatibility
- MP4 (H.264 High Quality) - Better quality, larger files
- MP4 (H.265/HEVC) - Smaller files, slower encoding
- WebM (VP9) - Web-optimized format
- MKV (H.264) - Matroska container
- AVI (MPEG-4) - Legacy format

**Supported input formats:** `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`, `.mp4`, `.m4v`, `.mpeg`, `.mpg`

### Convert Audio

Converts audio files between formats.

**Available presets:**
- MP3 (320/192/128 kbps) - Universal compatibility
- AAC (256 kbps) - Modern format
- FLAC (Lossless) - No quality loss
- WAV (Uncompressed) - Raw audio
- OGG Vorbis - Open format
- Opus - Efficient codec

**Supported input formats:** `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`, `.wma`, `.mp3`, `.opus`

### Extract Audio

Extracts audio tracks from video files.

**Available presets:**
- Extract to MP3 (320/192 kbps)
- Extract to AAC
- Extract to WAV
- Extract to FLAC

**Supported input formats:** `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.m4v`

### Resize / Compress

Scales video resolution or reduces file size.

**Resolution presets:**
- 1080p (Full HD)
- 720p (HD)
- 480p (SD)
- 360p (Low)

**Compression presets:**
- High Quality - Minimal quality loss
- Medium Quality - Balanced
- Small File - Maximum compression

### Remux (No Re-encode)

Changes the container format without re-encoding. This is fast and lossless.

**Available conversions:**
- Remux to MP4
- Remux to MKV
- Remux to MOV
- Remux to WebM (requires VP8/VP9 video)

### Logs / Status

View application status and logs:
- FFmpeg availability status
- Log file size
- View recent log entries
- Clear log file

## Workflow Example

1. Copy your video files to the `import/` folder:
   ```
   import/
   ├── vacation_clip.mov
   ├── presentation.avi
   └── interview.mkv
   ```

2. Run MONICA:
   ```bash
   python main.py
   ```

3. Select "Convert video" from the menu

4. Choose a preset (e.g., "MP4 (H.264)")

5. Select files:
   - Use arrow keys to navigate
   - Press Space to select/deselect files
   - Press Enter when done

6. Confirm processing

7. Wait for completion:
   - Progress bar shows conversion status
   - Each file is processed one at a time

8. Find your converted files in `export/`:
   ```
   export/
   ├── vacation_clip_20260108_143210_MP4_converted.mp4
   ├── presentation_20260108_143245_MP4_converted.mp4
   └── interview_20260108_143312_MP4_converted.mp4
   ```

## Error Handling

### Conversion Fails

If a conversion fails:
1. Processing stops immediately
2. Error is logged
3. You're returned to the main menu
4. Check "Logs / status" for details

### No Files Found

If the file picker shows no files:
- Ensure files are in the `import/` folder
- Check that file extensions match the operation
- Video operations require video files
- Audio operations require audio files

### FFmpeg Issues

If FFmpeg download fails:
1. Check your internet connection
2. Try downloading manually:
   - Windows: https://ffmpeg.org/download.html#build-windows
   - Linux: `sudo apt install ffmpeg` or `sudo dnf install ffmpeg`
3. Ensure FFmpeg is in your system PATH

## Tips

- **Batch processing**: Select multiple files at once for efficient batch conversion
- **Check logs**: If something goes wrong, the logs contain detailed error information
- **Use remux for containers**: If you just need to change file format (MKV to MP4) without quality change, use "Remux" - it's instant
- **H.265 for storage**: Use H.265/HEVC for archival - smaller files with same quality
- **VP9 for web**: WebM with VP9 is optimized for web streaming
