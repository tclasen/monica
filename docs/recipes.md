# MONICA Recipes

Recipes are pre-configured FFmpeg command templates that define how media files are converted. This document explains how recipes work and how to create custom ones.

## Recipe Structure

Each recipe contains:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name in menus |
| `category` | string | One of: `video`, `audio`, `extract`, `resize`, `remux` |
| `extension` | string | Output file extension (e.g., `.mp4`) |
| `ffmpeg_args` | list | FFmpeg arguments for this conversion |
| `description` | string | Optional description shown in menu |
| `input_extensions` | list | Valid input file extensions |

## Example Recipe

```json
{
  "name": "MP4 (H.264)",
  "category": "video",
  "extension": ".mp4",
  "ffmpeg_args": ["-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "128k"],
  "description": "Standard MP4 with H.264 video and AAC audio",
  "input_extensions": [".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mp4"]
}
```

## FFmpeg Arguments Explained

### Video Encoding

| Argument | Description |
|----------|-------------|
| `-c:v libx264` | Use H.264 codec |
| `-c:v libx265` | Use H.265/HEVC codec |
| `-c:v libvpx-vp9` | Use VP9 codec |
| `-preset <speed>` | Encoding speed: ultrafast, fast, medium, slow, veryslow |
| `-crf <value>` | Quality (0-51, lower = better). 18-23 is typical |

### Audio Encoding

| Argument | Description |
|----------|-------------|
| `-c:a aac` | Use AAC codec |
| `-c:a libmp3lame` | Use MP3 codec |
| `-c:a libopus` | Use Opus codec |
| `-c:a flac` | Use FLAC codec |
| `-b:a 128k` | Audio bitrate |
| `-vn` | Remove video stream |

### Scaling

| Argument | Description |
|----------|-------------|
| `-vf scale=-2:1080` | Scale to 1080p height |
| `-vf scale=-2:720` | Scale to 720p height |
| `-vf scale=1920:-2` | Scale to 1920px width |

### Copy (No Re-encode)

| Argument | Description |
|----------|-------------|
| `-c copy` | Copy all streams without re-encoding |
| `-c:v copy` | Copy video without re-encoding |
| `-c:a copy` | Copy audio without re-encoding |

## Built-in Recipes

### Video Conversion

| Name | Codec | Quality | Use Case |
|------|-------|---------|----------|
| MP4 (H.264) | libx264 | CRF 23 | General purpose |
| MP4 (H.264 High Quality) | libx264 | CRF 18 | Archival |
| MP4 (H.265/HEVC) | libx265 | CRF 28 | Storage efficiency |
| WebM (VP9) | libvpx-vp9 | CRF 30 | Web streaming |
| MKV (H.264) | libx264 | CRF 23 | Flexible container |
| AVI (MPEG-4) | mpeg4 | q:v 5 | Legacy support |

### Audio Conversion

| Name | Codec | Bitrate | Use Case |
|------|-------|---------|----------|
| MP3 (320 kbps) | libmp3lame | 320k | High quality |
| MP3 (192 kbps) | libmp3lame | 192k | Standard |
| MP3 (128 kbps) | libmp3lame | 128k | Small files |
| AAC (256 kbps) | aac | 256k | Modern devices |
| FLAC (Lossless) | flac | N/A | Archival |
| WAV (Uncompressed) | pcm_s16le | N/A | Editing |
| OGG Vorbis | libvorbis | q:a 6 | Open format |
| Opus | libopus | 128k | Efficient |

### Resize/Compress

| Name | Resolution | Quality | Use Case |
|------|------------|---------|----------|
| 1080p (Full HD) | 1920x1080 | CRF 23 | High quality |
| 720p (HD) | 1280x720 | CRF 23 | Standard |
| 480p (SD) | 854x480 | CRF 23 | Mobile |
| 360p (Low) | 640x360 | CRF 25 | Thumbnails |
| Compress (High) | Original | CRF 20 | Slight reduction |
| Compress (Medium) | Original | CRF 26 | Balanced |
| Compress (Small) | Original | CRF 32 | Maximum |

## Custom Recipes

### Creating Custom Recipes

1. Create a file named `custom_recipes.json` in the project root:

```json
[
  {
    "name": "GIF from Video",
    "category": "video",
    "extension": ".gif",
    "ffmpeg_args": ["-vf", "fps=10,scale=320:-1:flags=lanczos", "-loop", "0"],
    "description": "Convert video to animated GIF",
    "input_extensions": [".mp4", ".mkv", ".avi", ".mov", ".webm"]
  },
  {
    "name": "Instagram Square (1080x1080)",
    "category": "resize",
    "extension": ".mp4",
    "ffmpeg_args": ["-vf", "scale=1080:1080:force_original_aspect_ratio=decrease,pad=1080:1080:(ow-iw)/2:(oh-ih)/2", "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "128k"],
    "description": "Square video for Instagram",
    "input_extensions": [".mp4", ".mkv", ".avi", ".mov"]
  }
]
```

2. Custom recipes will appear alongside built-in recipes in their respective category menus.

### Recipe Ideas

**Social Media:**
```json
{
  "name": "Twitter Video (720p, 40s max)",
  "category": "resize",
  "extension": ".mp4",
  "ffmpeg_args": ["-t", "40", "-vf", "scale=-2:720", "-c:v", "libx264", "-preset", "fast", "-crf", "23", "-c:a", "aac", "-b:a", "128k"],
  "description": "Optimized for Twitter upload",
  "input_extensions": [".mp4", ".mkv", ".avi", ".mov"]
}
```

**Slow Motion:**
```json
{
  "name": "2x Slow Motion",
  "category": "video",
  "extension": ".mp4",
  "ffmpeg_args": ["-filter:v", "setpts=2.0*PTS", "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-an"],
  "description": "Half speed (no audio)",
  "input_extensions": [".mp4", ".mkv", ".avi", ".mov"]
}
```

**Audio Normalization:**
```json
{
  "name": "MP3 Normalized",
  "category": "audio",
  "extension": ".mp3",
  "ffmpeg_args": ["-vn", "-af", "loudnorm", "-c:a", "libmp3lame", "-b:a", "320k"],
  "description": "MP3 with volume normalization",
  "input_extensions": [".wav", ".flac", ".mp3", ".m4a"]
}
```

## Tips

- Start with a built-in recipe and modify the FFmpeg arguments
- Test recipes with a short clip before batch processing
- Use CRF for quality-based encoding (consistent quality, variable file size)
- Use bitrate for size-based encoding (consistent size, variable quality)
- Lower CRF values = higher quality = larger files
- Slower presets = better compression = longer encoding time
