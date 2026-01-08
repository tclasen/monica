# YouTube Optimization Guide

This guide explains how to prepare videos for YouTube using MONICA's dedicated YouTube presets.

## Why YouTube Needs Special Settings

YouTube re-encodes every video you upload. Even if you upload a 10 GB master file, YouTube will compress it for streaming. However, starting with a well-optimized source file gives YouTube the best possible input, resulting in better final quality.

### YouTube's Processing Pipeline

1. You upload your video
2. YouTube analyzes and re-encodes it
3. Multiple quality versions are created (144p to 4K)
4. Viewers stream the appropriate quality

**Key insight**: YouTube's encoding is optimized for H.264/AAC input. Giving it a well-encoded source means less quality loss in processing.

---

## MONICA's YouTube Presets

Access these from the main menu under **YouTube**.

### Resolution Presets

#### YouTube 4K (2160p)
```
Resolution: 3840x2160 (scaled to 2160p height)
Video: H.264, CRF 18, slow preset
Audio: AAC 384 kbps, 48 kHz
```

**Best for**: 4K footage, high-end production, maximum quality

**File size**: Large (~8-15 GB per hour)

**When to use**: When your source is 4K and you want the best possible YouTube quality.

#### YouTube 1080p (Full HD)
```
Resolution: 1920x1080 (scaled to 1080p height)
Video: H.264, CRF 20, medium preset
Audio: AAC 384 kbps, 48 kHz
```

**Best for**: Standard HD content, most uploads

**File size**: Moderate (~3-5 GB per hour)

**When to use**: Your default choice for most content. This is what most successful YouTubers use.

#### YouTube 720p (HD)
```
Resolution: 1280x720 (scaled to 720p height)
Video: H.264, CRF 20, medium preset
Audio: AAC 256 kbps, 48 kHz
```

**Best for**: Faster uploads, bandwidth-limited connections

**File size**: Smaller (~1.5-2.5 GB per hour)

**When to use**: When upload speed matters more than maximum quality, or your source is 720p.

#### YouTube 480p (SD)
```
Resolution: 854x480 (scaled to 480p height)
Video: H.264, CRF 22, medium preset
Audio: AAC 128 kbps, 48 kHz
```

**Best for**: Very slow connections, minimal file sizes

**File size**: Small (~500 MB - 1 GB per hour)

**When to use**: Emergency uploads, extremely limited bandwidth.

### YouTube Shorts Presets

YouTube Shorts are vertical videos (9:16 aspect ratio) up to 60 seconds.

#### YouTube Shorts (1080x1920)
```
Resolution: 1080x1920 (vertical Full HD)
Video: H.264, CRF 20
Audio: AAC 256 kbps
```

**Best for**: High-quality Shorts

**Note**: Automatically adds letterboxing/pillarboxing if source isn't 9:16.

#### YouTube Shorts (720x1280)
```
Resolution: 720x1280 (vertical HD)
Video: H.264, CRF 22
Audio: AAC 192 kbps
```

**Best for**: Smaller Shorts files, faster upload

### Quality Presets

#### YouTube High Quality
```
Resolution: Original (no scaling)
Video: H.264, CRF 17, slow preset
Audio: AAC 384 kbps
```

**Best for**: Maximum quality when you don't need to change resolution

**File size**: Large

**When to use**: Professional content, music videos, cinematic work.

#### YouTube Fast Upload
```
Resolution: Original
Video: H.264, CRF 23, fast preset
Audio: AAC 256 kbps
```

**Best for**: Quick encoding, reasonable quality

**File size**: Moderate

**When to use**: When you need to upload quickly and quality is secondary.

#### YouTube Small File
```
Resolution: 720p
Video: H.264, CRF 26
Audio: AAC 128 kbps
```

**Best for**: Minimum file size while remaining acceptable

**File size**: Small

**When to use**: Very slow internet, testing, draft uploads.

---

## YouTube's Recommended Settings

These are YouTube's official recommendations, which MONICA's presets follow:

### Container
- **Format**: MP4
- **Moov atom**: At front (faststart flag) - enables streaming

### Video Codec
- **Codec**: H.264
- **Profile**: High
- **Frame rate**: Same as source (24, 25, 30, 50, 60 fps)
- **Chroma subsampling**: 4:2:0

### Audio Codec
- **Codec**: AAC-LC
- **Channels**: Stereo or 5.1
- **Sample rate**: 48 kHz (YouTube's native rate)

### Bitrate Recommendations by Resolution

| Resolution | Video Bitrate (SDR) | Video Bitrate (HDR) |
|------------|--------------------|--------------------|
| 2160p (4K) | 35-45 Mbps | 44-56 Mbps |
| 1440p | 16 Mbps | 20 Mbps |
| 1080p | 8 Mbps | 10 Mbps |
| 720p | 5 Mbps | 6.5 Mbps |
| 480p | 2.5 Mbps | N/A |

MONICA uses CRF (Constant Rate Factor) instead of fixed bitrate, which adapts to scene complexity for better quality.

---

## Choosing the Right Preset

### Quick Decision Guide

```
Is your source 4K?
├── Yes → YouTube 4K (2160p)
└── No
    ├── Is it 1080p or higher? → YouTube 1080p
    └── Is it 720p or lower? → YouTube 720p
```

### By Content Type

| Content Type | Recommended Preset |
|--------------|-------------------|
| Gaming | 1080p or 4K (High Quality) |
| Vlog | 1080p |
| Tutorial/Screencast | 1080p |
| Music video | High Quality |
| Podcast (with video) | 720p or 1080p |
| Shorts | Shorts 1080x1920 |

### By Upload Situation

| Situation | Recommended Preset |
|-----------|-------------------|
| Plenty of time | High Quality |
| Normal upload | 1080p |
| Need it fast | Fast Upload |
| Slow internet | Small File or 720p |

---

## YouTube Shorts Explained

YouTube Shorts are:
- Vertical videos (9:16 aspect ratio)
- Up to 60 seconds long
- Optimized for mobile viewing
- Shown in the Shorts shelf

### Creating Shorts from Horizontal Video

If your source is horizontal (16:9), MONICA's Shorts presets will:
1. Scale to fit the vertical frame
2. Add black bars (letterboxing) to fill the space

For best results, crop to 9:16 in video editing software first.

### Shorts Best Practices

1. **Hook in first 2 seconds** - Viewers scroll quickly
2. **Use vertical space** - Don't waste screen with letterboxing
3. **Clear audio** - Many watch with sound on (unlike regular mobile)
4. **Fast pacing** - Keep it snappy

---

## Upload Optimization Tips

### 1. Use Faststart

All MONICA YouTube presets include `-movflags +faststart`. This moves metadata to the file's beginning, allowing YouTube to start processing immediately.

### 2. Match Frame Rate

Don't convert 24fps to 30fps or vice versa. MONICA preserves original frame rates.

### 3. Avoid Re-encoding

If your video is already H.264/AAC in MP4:
- Check if it meets YouTube specs
- Consider direct upload without conversion
- Only convert if quality or file size needs improvement

### 4. Upload During Off-Peak Hours

YouTube processing is faster when their servers are less busy (typically late night/early morning).

### 5. Use Wired Internet

For large files, wired connections are more reliable than WiFi.

---

## Common YouTube Issues

### Video Looks Blurry After Upload

**Cause**: YouTube hasn't finished processing HD versions yet.

**Solution**: Wait 30-60 minutes. YouTube processes lower resolutions first.

### Quality Worse Than Original

**Cause**: YouTube's re-encoding reduced quality.

**Solution**: Upload higher quality source. Use YouTube High Quality preset.

### Audio Sync Issues

**Cause**: Variable frame rate in source file.

**Solution**: Convert to constant frame rate (MONICA handles this).

### Upload Stuck/Failed

**Causes**:
- Unstable internet
- File too large
- Unsupported format

**Solutions**:
- Use a smaller preset
- Check internet stability
- Ensure H.264/AAC in MP4

### Video Processing Takes Forever

**Cause**: Very long videos, 4K content, high complexity.

**Solution**: Be patient. 4K videos can take hours to process fully.

---

## File Size Expectations

Approximate sizes for 10-minute videos:

| Preset | Expected Size |
|--------|--------------|
| YouTube 4K | 1.5 - 2.5 GB |
| YouTube 1080p | 500 MB - 1 GB |
| YouTube 720p | 250 - 500 MB |
| YouTube 480p | 80 - 200 MB |
| Shorts (1 minute) | 20 - 50 MB |

---

## Step-by-Step: Upload Workflow

### Standard Video

1. **Edit your video** in your preferred editor
2. **Export** from editor (high quality)
3. **Add to MONICA** `import/` folder
4. **Select YouTube** from main menu
5. **Choose preset** (1080p for most cases)
6. **Process** and wait for completion
7. **Upload** the file from `export/` to YouTube

### YouTube Short

1. **Edit your vertical video** (< 60 seconds)
2. **Add to MONICA** `import/` folder
3. **Select YouTube** → **YouTube Shorts (1080x1920)**
4. **Process** and upload
5. **Add #Shorts** to title or description (helps YouTube identify it)

---

## Pro Tips

### 1. Two-Pass for Best Quality

For maximum quality on important videos, consider:
- First: Export from editor at very high quality
- Second: Convert with MONICA's YouTube High Quality preset

### 2. Test Processing

Upload a short clip first to verify everything looks correct before uploading a long video.

### 3. Schedule Uploads

Convert videos in batch, then schedule uploads through YouTube Studio.

### 4. Keep Source Files

Always keep your original exports. YouTube settings may change, and you might need to re-upload.

---

## Next Steps

- [Video Conversion Guide](video-conversion.md) - Understanding codecs
- [Formats Explained](formats-explained.md) - Complete format reference
- [Troubleshooting](troubleshooting.md) - Fix common issues
