# Audio Conversion Guide

This guide covers everything about converting audio files and extracting audio from video with MONICA.

## Audio Operations in MONICA

MONICA offers two audio-related operations:

1. **Convert Audio** - Convert between audio formats (MP3, FLAC, WAV, etc.)
2. **Extract Audio** - Pull the audio track out of video files

---

## Lossy vs Lossless: The Fundamental Choice

Before choosing a format, understand this key distinction:

### Lossy Formats

**What it means**: Some audio data is permanently discarded to reduce file size.

**Formats**: MP3, AAC, OGG Vorbis, Opus

**Pros**:
- Much smaller files (10-20x smaller than lossless)
- Good enough for most listening
- Universal compatibility

**Cons**:
- Quality loss (though often imperceptible)
- Each re-conversion loses more quality
- Can't recover original quality

### Lossless Formats

**What it means**: Audio is compressed without losing any data. Like ZIP for audio.

**Formats**: FLAC, WAV (uncompressed), ALAC

**Pros**:
- Perfect quality preservation
- Can convert to any format without additional loss
- Preferred for archiving and editing

**Cons**:
- Much larger files
- Overkill for casual listening
- Some devices don't support all formats

### The Golden Rule

```
Source → Lossless → Keep forever
Lossless → Lossy → For everyday use
Lossy → Lossy → Avoid if possible (quality degrades)
```

---

## Audio Format Deep Dive

### MP3 - The Universal Standard

**Extension**: `.mp3`
**Type**: Lossy
**Compatibility**: Everything

MP3 has been around since 1993 and is supported by literally every audio device ever made. While technically inferior to newer codecs, its universal support makes it the safest choice for sharing.

#### Bitrate Guide

| Bitrate | Quality | File Size | Use Case |
|---------|---------|-----------|----------|
| 320 kbps | Excellent | ~2.4 MB/min | Music lovers, permanent collection |
| 256 kbps | Very good | ~1.9 MB/min | High-quality general use |
| 192 kbps | Good | ~1.4 MB/min | Streaming, podcasts |
| 128 kbps | Acceptable | ~1.0 MB/min | Voice, audiobooks, background music |

**Recommendation**: Use 320 kbps for music, 192 kbps for speech.

### AAC - The Modern Choice

**Extension**: `.m4a`
**Type**: Lossy
**Compatibility**: Excellent (Apple, modern devices)

AAC is technically superior to MP3 - it sounds better at the same bitrate. Apple uses it for iTunes and all iOS devices. Most Android devices and modern media players support it too.

**When to use**: Apple ecosystem, when you want better quality than MP3 at the same size.

### FLAC - The Audiophile Format

**Extension**: `.flac`
**Type**: Lossless
**Compatibility**: Good (most players, not iTunes)

FLAC compresses audio to about 50-60% of the original size while preserving perfect quality. It's the standard for audiophiles and music archivists.

**When to use**:
- Archiving your music collection
- Source files for future conversions
- When quality matters more than size

**Note**: iTunes doesn't support FLAC. For Apple, use ALAC or convert to AAC.

### WAV - Pure Uncompressed

**Extension**: `.wav`
**Type**: Uncompressed (lossless)
**Compatibility**: Universal

WAV is raw, uncompressed audio. It's the standard format for audio editing and production. Files are large (~10 MB per minute for CD quality).

**When to use**:
- Audio editing/production
- When you need maximum compatibility
- Intermediate format for processing

### OGG Vorbis - The Open Alternative

**Extension**: `.ogg`
**Type**: Lossy
**Compatibility**: Good (not native on Apple)

An open-source, royalty-free format. Quality is comparable to AAC. Popular in games and open-source software.

**When to use**: Linux, game development, open-source projects.

### Opus - The Efficient Newcomer

**Extension**: `.opus`
**Type**: Lossy
**Compatibility**: Moderate (modern apps/browsers)

Opus is the most efficient audio codec available. At 128 kbps, it rivals MP3 at 256 kbps. Used by Discord, WhatsApp, and WebRTC.

**When to use**: Voice communication, streaming where bandwidth matters.

---

## MONICA's Audio Presets

### For Music

| Preset | Quality | Size | Best For |
|--------|---------|------|----------|
| MP3 (320 kbps) | ★★★★★ | Medium | Music collection |
| AAC (256 kbps) | ★★★★★ | Medium | Apple devices |
| FLAC | ★★★★★ | Large | Archival |

### For Voice/Podcasts

| Preset | Quality | Size | Best For |
|--------|---------|------|----------|
| MP3 (192 kbps) | ★★★★☆ | Small | Podcasts |
| MP3 (128 kbps) | ★★★☆☆ | Tiny | Voice only |
| Opus | ★★★★☆ | Tiny | Modern apps |

### For Editing

| Preset | Quality | Size | Best For |
|--------|---------|------|----------|
| WAV | ★★★★★ | Huge | Audio editing |
| FLAC | ★★★★★ | Large | Archive source |

---

## Extracting Audio from Video

One of MONICA's most useful features is extracting audio tracks from video files.

### Common Use Cases

- **Music videos**: Get the song without the video
- **Lectures/podcasts**: Audio-only for commuting
- **Movies**: Extract soundtrack or dialogue
- **Voice recordings**: Pull audio from video recordings

### How to Extract

1. Put your video file in `import/`
2. Select "Extract audio" from the main menu
3. Choose your output format:
   - **MP3 (320 kbps)** - Best quality, universal
   - **MP3 (192 kbps)** - Smaller files
   - **AAC** - Modern devices
   - **WAV** - For editing
   - **FLAC** - Lossless preservation
4. Select files and process

### Quality Considerations

When extracting audio, you can't get better quality than what's in the video:

| Video Audio | Extract to | Result |
|-------------|------------|--------|
| 128 kbps AAC | 320 kbps MP3 | Same quality, bigger file |
| 320 kbps AAC | 320 kbps MP3 | Good quality |
| Lossless | FLAC | Perfect quality |

**Tip**: If the source video has low-quality audio, extracting to a high bitrate won't improve it.

---

## Bitrate Guide: When to Use What

### Music

| Scenario | Recommended Format |
|----------|-------------------|
| Permanent collection | FLAC or MP3 320 kbps |
| Casual listening | MP3 192-256 kbps |
| Apple devices | AAC 256 kbps |
| Storage is limited | MP3 192 kbps |

### Voice/Speech

| Scenario | Recommended Format |
|----------|-------------------|
| Podcast distribution | MP3 192 kbps |
| Audiobook | MP3 128 kbps |
| Voice memo | MP3 128 kbps or Opus |
| Professional voiceover | WAV or FLAC |

### Sound Effects

| Scenario | Recommended Format |
|----------|-------------------|
| Game development | OGG or WAV |
| Video editing | WAV |
| Web use | MP3 or Opus |

---

## Best Practices

### 1. Start from the Best Source

Always convert from the highest quality source available:
- If you have the CD, rip to FLAC
- If you have FLAC, convert to MP3
- Avoid converting MP3 → MP3

### 2. Keep a Lossless Archive

For important audio:
1. Keep the original source (CD, vinyl rip, etc.)
2. Create a FLAC archive
3. Create MP3s for everyday use from the FLAC

### 3. Match Format to Use Case

Don't use 320 kbps MP3 for a voice memo. Don't use 128 kbps for your music collection.

### 4. Check Before Mass Converting

Test your settings on one file before batch converting hundreds.

### 5. Verify Output

Always spot-check converted files before deleting originals.

---

## Common Questions

### Is 320 kbps MP3 as good as FLAC?

For most listeners, no audible difference. In blind tests, most people can't distinguish them. However:
- FLAC is technically perfect
- MP3 loses some data (even if imperceptible)
- FLAC can be converted later; MP3 quality is fixed

### Should I convert my MP3s to FLAC?

No! Converting lossy to lossless doesn't recover quality. You just get a bigger file with the same quality.

### Why is my extracted audio quiet?

The source video might have quiet audio. MONICA preserves the original levels. Use audio editing software to normalize if needed.

### Can I convert video to audio directly?

Yes! Use "Extract audio" in MONICA. It extracts only the audio track and saves it in your chosen format.

### What's the best format for podcasts?

MP3 at 192 kbps is the industry standard. Universal compatibility and small file sizes.

---

## Quick Reference

### Quality Rankings (for same bitrate)

1. **Opus** - Best efficiency
2. **AAC** - Great efficiency
3. **Vorbis** - Good efficiency
4. **MP3** - Baseline

### File Size (per minute, stereo)

| Format | Size |
|--------|------|
| WAV (CD quality) | ~10 MB |
| FLAC | ~5-6 MB |
| MP3 320 kbps | ~2.4 MB |
| MP3 192 kbps | ~1.4 MB |
| MP3 128 kbps | ~1.0 MB |

---

## Next Steps

- [Formats Explained](formats-explained.md) - Complete format reference
- [Advanced Tips](advanced-tips.md) - Power user features
- [Troubleshooting](troubleshooting.md) - Fix common issues
