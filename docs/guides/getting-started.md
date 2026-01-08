# Getting Started with MONICA

Welcome to MONICA! This guide will walk you through everything you need to know to start converting media files.

## What is MONICA?

**MONICA** stands for **M**edia **O**perations **N**avigator with **I**nteractive **C**ommand-line **A**ssistance.

It's a friendly command-line tool that makes FFmpeg easy to use. Instead of memorizing complex commands like:

```bash
ffmpeg -i input.avi -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k output.mp4
```

You simply:
1. Pick "Convert video" from a menu
2. Choose "MP4 (H.264)"
3. Select your files
4. Done!

MONICA handles all the technical details for you.

---

## Installation

### Prerequisites

- **Python 3.10 or higher**
- **FFmpeg** (MONICA can download this automatically)

### Step 1: Get the Code

```bash
git clone https://github.com/yourusername/monica.git
cd monica
```

Or download and extract the ZIP file.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs three small packages:
- `questionary` - For the interactive menus
- `colorama` - For colored text in the terminal
- `requests` - For downloading FFmpeg if needed

### Step 3: Run MONICA

```bash
python main.py
```

That's it! On first run, MONICA will:
1. Create the necessary folders
2. Check for FFmpeg (and offer to download it if missing)
3. Launch the main menu

---

## First Run Walkthrough

When you run MONICA for the first time, here's what happens:

### 1. Folder Creation

MONICA automatically creates three folders:

```
monica/
├── import/    <- Put your source files here
├── export/    <- Converted files appear here
└── logs/      <- Log files for troubleshooting
```

### 2. FFmpeg Check

```
Checking FFmpeg availability...
[OK] FFmpeg is available
```

If FFmpeg isn't installed, you'll see:

```
[X] FFmpeg not found

FFmpeg is required to use MONICA.
Would you like to download it automatically? (Y/n)
```

Press Enter (or Y) to download automatically. MONICA will:
- Detect your operating system
- Download the appropriate FFmpeg build
- Extract it to a local folder
- Verify it works

### 3. Main Menu

Once setup is complete, you'll see the main menu:

```
╔══════════════════════════════════════════╗
║  MONICA - FFmpeg Interactive CLI Tool    ║
╚══════════════════════════════════════════╝

? Main Menu:
> Convert video
  Convert audio
  Extract audio
  Resize / compress
  Remux (no re-encode)
  YouTube
  Logs / status
  Help
  Exit
```

Use the **arrow keys** to navigate and **Enter** to select.

---

## Your First Conversion

Let's convert a video file to MP4. Here's the complete workflow:

### Step 1: Add Files to Import

Copy your video file(s) to the `import/` folder:

```
import/
└── my_video.avi
```

### Step 2: Select Operation

Run MONICA and choose "Convert video":

```
? Main Menu: Convert video
```

### Step 3: Choose a Preset

Select your desired format:

```
? Select a preset:
> MP4 (H.264) - Standard MP4 with H.264 video and AAC audio
  MP4 (H.264 High Quality) - High quality MP4 with better compression
  MP4 (H.265/HEVC) - MP4 with H.265 video (smaller files, slower encode)
  ...
```

For most cases, "MP4 (H.264)" is the best choice.

### Step 4: Select Files

Use **Space** to select files, then **Enter** to confirm:

```
? Select files to process:
> [X] my_video.avi (150.3 MB)
  [ ] another_video.mkv (2.1 GB)
```

### Step 5: Confirm and Process

```
Selected 1 file(s):
  - my_video.avi

? Start processing? (Y/n)
```

Press Enter to begin. You'll see a progress bar:

```
[1/1] my_video.avi
    -> my_video_20260108_143210_MP4_converted.mp4
[========================================] 100.0%
Done!

All 1 file(s) processed successfully!
```

### Step 6: Get Your File

Your converted file is now in the `export/` folder:

```
export/
└── my_video_20260108_143210_MP4_converted.mp4
```

---

## Folder Structure Explained

### `/import` - Input Files

This is where you put files you want to convert. MONICA only reads from this folder - your original files are never modified.

**Supported input formats:**
- Video: .mp4, .mkv, .avi, .mov, .wmv, .flv, .webm, .m4v, .mpeg, .mpg
- Audio: .mp3, .wav, .flac, .aac, .ogg, .m4a, .wma, .opus

### `/export` - Output Files

All converted files are saved here with a timestamp in the filename:

```
<original_name>_<YYYYMMDD_HHMMSS>_<FORMAT>_converted.<extension>
```

Example: `vacation_20260108_143210_MP4_converted.mp4`

This naming scheme:
- Prevents overwriting files
- Shows when conversion happened
- Indicates the output format

### `/logs` - Log Files

MONICA keeps detailed logs of all operations. Useful for:
- Troubleshooting failed conversions
- Reviewing what was converted
- Checking for errors

View logs from the "Logs / status" menu option.

---

## Keyboard Controls

| Key | Action |
|-----|--------|
| **↑ / ↓** | Navigate menu options |
| **Enter** | Select / Confirm |
| **Space** | Toggle file selection (in file picker) |
| **Ctrl+C** | Cancel / Exit |

---

## Quick Tips

1. **Start with MP4 (H.264)** - It's the most compatible format and works everywhere.

2. **Use Remux for container changes** - If you just need MKV → MP4 without changing quality, use "Remux" - it's instant!

3. **Check the logs** - If something goes wrong, the logs usually explain why.

4. **Keep your originals** - Always verify converted files before deleting sources.

5. **Batch process overnight** - Select multiple files and let MONICA work while you sleep.

---

## Next Steps

Now that you're set up, explore these guides:

- [Video Conversion Guide](video-conversion.md) - Deep dive into video formats
- [Audio Conversion Guide](audio-conversion.md) - Everything about audio
- [YouTube Guide](youtube-guide.md) - Optimize for YouTube uploads
- [Formats Explained](formats-explained.md) - Complete format reference
- [Troubleshooting](troubleshooting.md) - Common issues and solutions
- [Advanced Tips](advanced-tips.md) - Power user features

---

## Getting Help

- **In-app help**: Select "Help" from the main menu
- **Documentation**: Check the `docs/` folder
- **Issues**: Report bugs on GitHub
