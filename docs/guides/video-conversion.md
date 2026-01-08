# Video Conversion Guide

This guide explains everything you need to know about converting video files with MONICA.

## When to Convert Video

You should convert video when:

- **Compatibility**: Your device can't play the file (e.g., Apple TV won't play MKV)
- **File size**: The video is too large and you need to compress it
- **Uploading**: A platform requires a specific format (YouTube, Vimeo, etc.)
- **Editing**: Your video editor doesn't support the codec
- **Archiving**: You want to standardize your video library

You should **NOT** convert when:

- You only need to change the container (MKV to MP4) - use **Remux** instead
- The file already plays fine everywhere
- You want to maintain maximum quality without any loss

---

## Understanding Containers vs Codecs

This is the most important concept in video conversion.

### Containers (File Extensions)

The **container** is the "box" that holds the video and audio data. It's what you see as the file extension.

| Container | Extension | Description |
|-----------|-----------|-------------|
| MP4 | .mp4 | Universal standard, works everywhere |
| MKV | .mkv | Feature-rich, supports everything |
| WebM | .webm | Web-optimized, open-source |
| AVI | .avi | Legacy format from Windows |
| MOV | .mov | Apple's format |

### Codecs (Compression)

The **codec** is the actual compression algorithm used for video and audio inside the container.

| Codec | Type | Description |
|-------|------|-------------|
| H.264 (AVC) | Video | Universal, fast, good quality |
| H.265 (HEVC) | Video | Better compression, slower |
| VP9 | Video | Google's codec, used by YouTube |
| AAC | Audio | Modern, efficient |
| MP3 | Audio | Universal but older |

### The Key Insight

**A container can hold different codecs.**

For example, an MP4 file could contain:
- H.264 video + AAC audio (most common)
- H.265 video + AAC audio
- MPEG-4 video + MP3 audio

This is why two `.mp4` files might behave differently - they might have different codecs inside!

---

## MONICA's Video Presets

### MP4 (H.264) - The Safe Choice

```
Best for: General use, sharing, maximum compatibility
Quality: ★★★★☆
Speed: ★★★★☆
File size: ★★★☆☆
```

This is the default recommendation. H.264 video with AAC audio plays on:
- All smartphones (iOS, Android)
- All computers (Windows, Mac, Linux)
- All smart TVs
- All web browsers
- Game consoles (PlayStation, Xbox)

**When to use**: When you're not sure what to pick, pick this.

### MP4 (H.264 High Quality)

```
Best for: Archiving important videos
Quality: ★★★★★
Speed: ★★★☆☆
File size: ★★☆☆☆
```

Uses slower encoding with lower CRF (better quality) for visually demanding content. Files are larger but look better.

**When to use**: Wedding videos, professional work, anything where quality matters most.

### MP4 (H.265/HEVC)

```
Best for: Saving storage space
Quality: ★★★★★
Speed: ★★☆☆☆
File size: ★★★★★
```

H.265 achieves the same quality as H.264 at roughly **half the file size**. The tradeoff is slower encoding (2-3x longer) and slightly less compatibility.

**When to use**:
- Large video libraries where storage matters
- 4K content (file sizes get huge otherwise)
- Archival when you have time to encode

**Compatibility note**: Most devices from 2017+ support H.265, but some older devices don't.

### WebM (VP9)

```
Best for: Web streaming
Quality: ★★★★★
Speed: ★★☆☆☆
File size: ★★★★☆
```

Google's open-source codec. Excellent quality and supported by all modern browsers. YouTube uses VP9 for most of its videos.

**When to use**: Web projects, open-source work, or when you need royalty-free formats.

### MKV (H.264)

```
Best for: Archiving with metadata
Quality: ★★★★☆
Speed: ★★★★☆
File size: ★★★☆☆
```

Same quality as MP4 but in the MKV container. MKV supports:
- Multiple audio tracks
- Multiple subtitle tracks
- Chapters
- Attachments (fonts, etc.)

**When to use**: Movies with multiple audio languages, content with subtitles.

### AVI (MPEG-4)

```
Best for: Legacy devices
Quality: ★★★☆☆
Speed: ★★★★★
File size: ★★☆☆☆
```

Older format using MPEG-4 video. Only use this for compatibility with very old devices or software.

**When to use**: Old DVD players, legacy systems.

---

## Quality vs File Size

### Understanding CRF (Constant Rate Factor)

MONICA uses CRF for quality control. Lower numbers = better quality = larger files.

| CRF | Quality | Use Case |
|-----|---------|----------|
| 17-18 | Visually lossless | Archival, professional |
| 20-22 | High quality | General use |
| 23-25 | Good quality | Default balance |
| 26-28 | Medium quality | Saving space |
| 30+ | Lower quality | Maximum compression |

### Typical File Size Examples

Converting a 1-hour 1080p video:

| Preset | Approximate Size |
|--------|------------------|
| MP4 H.264 (default) | ~2-3 GB |
| MP4 H.264 High Quality | ~4-5 GB |
| MP4 H.265 | ~1-1.5 GB |
| Compressed (Medium) | ~1.5-2 GB |
| Compressed (Small) | ~800 MB - 1 GB |

*Actual sizes vary based on content complexity.*

---

## Step-by-Step Conversion Tutorial

### Scenario: Convert MKV to MP4 for iPhone

1. **Copy your MKV file** to the `import/` folder

2. **Run MONICA**
   ```bash
   python main.py
   ```

3. **Select "Convert video"** from the main menu

4. **Choose "MP4 (H.264)"** - iPhones fully support this

5. **Select your file** using Space, then Enter

6. **Confirm** when prompted

7. **Wait for conversion** - watch the progress bar

8. **Get your file** from the `export/` folder

9. **Transfer to iPhone** via iTunes, AirDrop, or your preferred method

### Scenario: Compress a Large Video

1. **Add file** to `import/`

2. **Select "Resize / compress"** from the menu

3. **Choose compression level**:
   - "Compress (High Quality)" - minimal quality loss
   - "Compress (Medium Quality)" - noticeable but acceptable
   - "Compress (Small File)" - maximum compression

4. **Process and retrieve** from `export/`

---

## Common Questions

### Should I always convert to MP4?

No! MP4 is great for compatibility, but:
- Use **MKV** if you need multiple audio/subtitle tracks
- Use **WebM** for web-only content
- Use **Remux** if you just need a container change

### Will I lose quality when converting?

Yes, but it depends:
- **Lossy to lossy** (MP4 to MP4): Some quality loss
- **Remux**: Zero quality loss (just changes container)
- **High quality presets**: Minimal visible loss

Rule of thumb: Avoid converting the same file multiple times.

### Why is H.265 so slow?

H.265 is computationally complex - it analyzes the video more thoroughly to achieve better compression. The tradeoff is encoding time.

Tips for faster H.265:
- Use a faster preset (MONICA uses "medium")
- Consider hardware encoding if available
- Encode overnight for large files

### What's the difference between Convert and Remux?

| Feature | Convert | Remux |
|---------|---------|-------|
| Speed | Slow | Instant |
| Quality | Some loss | No loss |
| File size | Can reduce | Same |
| Codec change | Yes | No |

Use **Remux** when you only need to change the container (MKV → MP4) and the codec is already compatible.

---

## Best Practices

1. **Always keep originals** until you verify the conversion

2. **Don't upscale** - Converting 720p to 1080p doesn't add quality

3. **Match your use case**:
   - Sharing? Use MP4 H.264
   - Archiving? Use H.265 or High Quality
   - Web? Use WebM

4. **Check before batch converting** - Test with one file first

5. **Use Remux when possible** - It's instant and lossless

---

## Next Steps

- [Formats Explained](formats-explained.md) - Complete format reference
- [YouTube Guide](youtube-guide.md) - Optimize for YouTube
- [Troubleshooting](troubleshooting.md) - Fix common issues
