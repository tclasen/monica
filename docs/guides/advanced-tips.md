# Advanced Tips & Tricks

This guide covers power user features and optimization strategies for MONICA.

---

## Batch Processing Strategies

### Planning Large Batches

When converting many files:

1. **Test first**: Always test your settings on 1-2 files before processing hundreds
2. **Sort by type**: Group similar files (same resolution, codec) together
3. **Check disk space**: Estimate output size × number of files
4. **Schedule wisely**: Run overnight for large batches

### Organizing Your Workflow

```
Day 1: Collect files → import/
Day 1: Test conversion on sample
Day 1: Start batch before bed
Day 2: Verify outputs
Day 2: Archive or delete originals
```

### Estimating Time

Rough encoding speeds (varies by CPU):

| Content | Preset | Speed |
|---------|--------|-------|
| 1080p H.264 medium | ~40-60 fps | ~Real-time |
| 1080p H.264 slow | ~15-25 fps | ~2-3x real-time |
| 1080p H.265 medium | ~15-30 fps | ~2-3x real-time |
| 4K H.264 medium | ~10-20 fps | ~3-5x real-time |
| 4K H.265 medium | ~5-10 fps | ~6-10x real-time |

**Example**: 10 one-hour 1080p videos with H.264 medium ≈ 10-20 hours

### Priority Order

If you have mixed content, prioritize:
1. **Urgent files first**: Need them soon
2. **Smaller files**: Quick wins build momentum
3. **Similar settings**: Minimize menu navigation
4. **Large files last**: Run overnight

---

## Understanding Quality Settings

### CRF (Constant Rate Factor)

CRF controls quality vs. file size. Lower = better quality = larger files.

| CRF | Quality Level | Use Case |
|-----|---------------|----------|
| 0 | Lossless | Not recommended (huge files) |
| 15-17 | Visually lossless | Professional/archival |
| 18-20 | Excellent | High quality needs |
| 21-23 | Very good | Default balance |
| 24-26 | Good | Saving space |
| 27-30 | Acceptable | Maximum compression |
| 31+ | Low | Emergency only |

**Rule of thumb**:
- +6 CRF ≈ half the file size
- -6 CRF ≈ double the file size

### Preset Speed vs Quality

Presets trade encoding time for compression efficiency:

| Preset | Encoding Speed | File Size | Quality |
|--------|----------------|-----------|---------|
| ultrafast | 10x | Largest | Lowest |
| superfast | 6x | Very large | Low |
| veryfast | 4x | Large | Below average |
| faster | 3x | Above average | Average |
| fast | 2x | Average | Good |
| **medium** | **1x (baseline)** | **Baseline** | **Good** |
| slow | 0.5x | Smaller | Better |
| slower | 0.3x | Much smaller | Much better |
| veryslow | 0.1x | Smallest | Best |

**Key insight**: Same CRF + slower preset = smaller file at identical visual quality.

### Choosing the Right Combination

| Priority | CRF | Preset | Result |
|----------|-----|--------|--------|
| Quality | 18-20 | slow | Best quality, larger files, slow |
| Balance | 22-23 | medium | Good quality, reasonable size |
| Speed | 23-25 | fast | Quick encoding, acceptable quality |
| Size | 26-28 | medium | Smaller files, visible compression |

---

## Optimal Settings by Use Case

### Personal Archive

**Goal**: Maximum quality, storage is available

```
Format: MKV or MP4
Codec: H.264 or H.265
CRF: 18-20
Preset: slow
Audio: FLAC or AAC 320kbps
```

Use H.265 for 50% space savings if playback compatibility isn't critical.

### Sharing with Others

**Goal**: Universal playback

```
Format: MP4
Codec: H.264
CRF: 20-23
Preset: medium
Audio: AAC 192kbps
```

### Mobile Devices

**Goal**: Small files, battery-friendly playback

```
Format: MP4
Codec: H.264
Resolution: 720p
CRF: 23-25
Audio: AAC 128kbps
```

### Streaming Server (Plex/Jellyfin)

**Goal**: Direct play without transcoding

```
Format: MP4 or MKV
Codec: H.264 (most compatible) or H.265 (for newer clients)
CRF: 20-23
Audio: AAC (or keep original)
```

### Long-term Storage

**Goal**: Future-proof, space-efficient

```
Format: MKV
Codec: H.265
CRF: 20-22
Preset: slow
Audio: FLAC (or original)
```

---

## Creating Custom Recipes

MONICA supports custom recipes via JSON files.

### Recipe Structure

Create a file called `custom_recipes.json` in the MONICA folder:

```json
[
  {
    "name": "My Custom Preset",
    "category": "video",
    "extension": ".mp4",
    "ffmpeg_args": [
      "-c:v", "libx264",
      "-preset", "slow",
      "-crf", "20",
      "-c:a", "aac",
      "-b:a", "192k"
    ],
    "description": "My personal high-quality preset",
    "input_extensions": [".mkv", ".avi", ".mov", ".mp4"]
  }
]
```

### Recipe Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name in menu |
| `category` | string | video, audio, extract, resize, remux, youtube |
| `extension` | string | Output file extension (e.g., ".mp4") |
| `ffmpeg_args` | array | FFmpeg arguments |
| `description` | string | Shown in menu |
| `input_extensions` | array | Valid input formats |

### Example Custom Recipes

#### Instagram Square Video
```json
{
  "name": "Instagram Square (1080x1080)",
  "category": "resize",
  "extension": ".mp4",
  "ffmpeg_args": [
    "-vf", "scale=1080:1080:force_original_aspect_ratio=decrease,pad=1080:1080:(ow-iw)/2:(oh-ih)/2",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "23",
    "-c:a", "aac",
    "-b:a", "128k"
  ],
  "description": "Square format for Instagram feed",
  "input_extensions": [".mp4", ".mkv", ".avi", ".mov"]
}
```

#### Twitter Video (720p, 140s max)
```json
{
  "name": "Twitter Video",
  "category": "resize",
  "extension": ".mp4",
  "ffmpeg_args": [
    "-t", "140",
    "-vf", "scale=-2:720",
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "23",
    "-c:a", "aac",
    "-b:a", "128k"
  ],
  "description": "Optimized for Twitter (720p, max 2:20)",
  "input_extensions": [".mp4", ".mkv", ".avi", ".mov"]
}
```

#### Podcast Audio (Mono, Normalized)
```json
{
  "name": "Podcast (Mono 96kbps)",
  "category": "audio",
  "extension": ".mp3",
  "ffmpeg_args": [
    "-vn",
    "-ac", "1",
    "-af", "loudnorm",
    "-c:a", "libmp3lame",
    "-b:a", "96k"
  ],
  "description": "Mono MP3 with loudness normalization",
  "input_extensions": [".wav", ".flac", ".mp3", ".m4a"]
}
```

#### GIF from Video
```json
{
  "name": "Animated GIF",
  "category": "video",
  "extension": ".gif",
  "ffmpeg_args": [
    "-vf", "fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
    "-loop", "0"
  ],
  "description": "Convert video to animated GIF (480px wide)",
  "input_extensions": [".mp4", ".mkv", ".avi", ".mov", ".webm"]
}
```

---

## FFmpeg Arguments Reference

Common arguments you might use in custom recipes:

### Video

| Argument | Effect |
|----------|--------|
| `-c:v libx264` | Use H.264 codec |
| `-c:v libx265` | Use H.265 codec |
| `-preset <name>` | Encoding speed (ultrafast to veryslow) |
| `-crf <number>` | Quality (0-51, lower=better) |
| `-vf scale=-2:720` | Scale to 720p height |
| `-r 30` | Force 30 fps |
| `-pix_fmt yuv420p` | Pixel format (compatibility) |

### Audio

| Argument | Effect |
|----------|--------|
| `-c:a aac` | Use AAC codec |
| `-c:a libmp3lame` | Use MP3 codec |
| `-b:a 192k` | Audio bitrate |
| `-ar 48000` | Sample rate (48kHz) |
| `-ac 2` | Stereo (2 channels) |
| `-vn` | Remove video (audio only) |

### General

| Argument | Effect |
|----------|--------|
| `-t 60` | Limit to 60 seconds |
| `-ss 00:01:00` | Start at 1 minute |
| `-movflags +faststart` | Web streaming optimization |
| `-y` | Overwrite output |

---

## Hardware Acceleration

### What is Hardware Encoding?

Modern GPUs can encode video much faster than CPU. However:
- Slightly lower quality at same settings
- Limited codec support
- Driver-dependent

### NVIDIA (NVENC)

If you have an NVIDIA GPU, you can create custom recipes:

```json
{
  "name": "H.264 NVENC (Fast)",
  "category": "video",
  "extension": ".mp4",
  "ffmpeg_args": [
    "-c:v", "h264_nvenc",
    "-preset", "p4",
    "-rc", "vbr",
    "-cq", "23",
    "-c:a", "aac",
    "-b:a", "192k"
  ],
  "description": "GPU-accelerated H.264 encoding",
  "input_extensions": [".mkv", ".avi", ".mov", ".mp4"]
}
```

### AMD (AMF)

```json
{
  "name": "H.264 AMF (Fast)",
  "category": "video",
  "extension": ".mp4",
  "ffmpeg_args": [
    "-c:v", "h264_amf",
    "-quality", "balanced",
    "-c:a", "aac",
    "-b:a", "192k"
  ],
  "description": "AMD GPU-accelerated encoding",
  "input_extensions": [".mkv", ".avi", ".mov", ".mp4"]
}
```

### Intel Quick Sync

```json
{
  "name": "H.264 QSV (Fast)",
  "category": "video",
  "extension": ".mp4",
  "ffmpeg_args": [
    "-c:v", "h264_qsv",
    "-preset", "medium",
    "-global_quality", "23",
    "-c:a", "aac",
    "-b:a", "192k"
  ],
  "description": "Intel Quick Sync encoding",
  "input_extensions": [".mkv", ".avi", ".mov", ".mp4"]
}
```

**Note**: Hardware encoding requires proper drivers and FFmpeg built with appropriate support.

---

## Pro Tips

### 1. Two-Pass Encoding

For absolute best quality at a target file size, professionals use two-pass encoding. This isn't built into MONICA's presets, but you can create custom recipes for it.

### 2. Test Before Committing

Always test your settings on a short clip (30 seconds) before processing hours of footage.

### 3. Keep Metadata

Some conversions strip metadata (creation date, camera info). If this matters, research metadata preservation.

### 4. Lossless Intermediate

For complex workflows:
1. Convert to lossless (FFV1, ProRes)
2. Edit
3. Convert to final format

### 5. Monitor Progress

For very long jobs, check periodically that the process is still running and making progress.

### 6. Multiple Outputs

Need the same video in multiple formats? Convert to high-quality H.264 first, then convert from that to other formats.

### 7. Filename Conventions

MONICA's automatic naming prevents overwrites, but for organized libraries, consider renaming outputs after verification.

---

## Understanding Your Hardware

### CPU Cores and Encoding

More cores = faster encoding (mostly):
- 4 cores: Basic encoding
- 8 cores: Good for 1080p
- 16+ cores: Great for 4K and batch processing

### RAM Requirements

- 1080p encoding: 4-8 GB RAM
- 4K encoding: 8-16 GB RAM
- Multiple files: More RAM helps

### Storage Speed

- HDD: Fine for encoding, might be bottleneck for 4K
- SSD: Recommended for 4K, faster for all tasks
- NVMe: Overkill but ensures no bottleneck

---

## Next Steps

- [Formats Explained](formats-explained.md) - Deep dive into formats
- [Troubleshooting](troubleshooting.md) - Fix common issues
- [YouTube Guide](youtube-guide.md) - Optimize for YouTube
