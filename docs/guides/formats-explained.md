# Formats Explained: Complete Reference

This comprehensive guide covers all video and audio formats supported by MONICA.

---

## Video Containers

Containers are the "wrapper" that holds video, audio, and metadata together.

### MP4 (MPEG-4 Part 14)

**Extension**: `.mp4`, `.m4v`
**Developed by**: Moving Picture Experts Group
**Year**: 2001

#### Overview
MP4 is the most widely supported video container in existence. It's the default choice for web, mobile, and general distribution.

#### Pros
- Universal compatibility (plays on everything)
- Excellent streaming support
- Efficient metadata handling
- Industry standard

#### Cons
- Limited subtitle support (only certain formats)
- Can't hold all codec combinations
- Less flexible than MKV

#### Supported Codecs
| Video | Audio | Subtitles |
|-------|-------|-----------|
| H.264 | AAC | mov_text |
| H.265 | MP3 | tx3g |
| MPEG-4 | AC-3 | |
| VP9 | Opus | |

#### Best For
- Sharing videos
- Web playback
- Mobile devices
- YouTube uploads

#### Compatibility Chart
| Platform | Support |
|----------|---------|
| Windows | Native |
| macOS | Native |
| iOS | Native |
| Android | Native |
| Web browsers | Native |
| Smart TVs | Native |
| Game consoles | Native |

---

### MKV (Matroska)

**Extension**: `.mkv`
**Developed by**: Matroska.org
**Year**: 2002

#### Overview
MKV is the "Swiss Army knife" of containers. It can hold virtually anything and supports advanced features like multiple tracks and chapters.

#### Pros
- Supports any codec
- Multiple audio/subtitle tracks
- Chapters and metadata
- Attachments (fonts, images)
- Open-source and royalty-free

#### Cons
- Not supported on all devices
- Doesn't work on iOS without apps
- Some smart TVs struggle
- Not ideal for web streaming

#### Supported Codecs
| Video | Audio | Subtitles |
|-------|-------|-----------|
| Any | Any | SRT, ASS, SSA, PGS, VobSub |

#### Best For
- Archiving movies with extras
- Multiple language audio
- Anime (with styled subtitles)
- Personal media servers (Plex, Jellyfin)

#### Compatibility Chart
| Platform | Support |
|----------|---------|
| Windows | Native (with codecs) |
| macOS | VLC/third-party |
| iOS | Third-party apps |
| Android | Native (most devices) |
| Web browsers | Limited |
| Smart TVs | Varies |
| Plex/Jellyfin | Excellent |

---

### WebM

**Extension**: `.webm`
**Developed by**: Google
**Year**: 2010

#### Overview
WebM is designed specifically for web use. It's open-source, royalty-free, and supported by all modern browsers.

#### Pros
- Web-native (no plugins needed)
- Open and royalty-free
- Good compression (VP9)
- Supported by major browsers

#### Cons
- Limited to VP8/VP9 + Vorbis/Opus
- Not great for offline playback
- Less tooling support

#### Supported Codecs
| Video | Audio |
|-------|-------|
| VP8 | Vorbis |
| VP9 | Opus |
| AV1 | |

#### Best For
- Web embedding
- HTML5 video
- Open-source projects

#### Compatibility Chart
| Platform | Support |
|----------|---------|
| Chrome | Native |
| Firefox | Native |
| Edge | Native |
| Safari | Limited |
| Mobile browsers | Good |

---

### AVI (Audio Video Interleave)

**Extension**: `.avi`
**Developed by**: Microsoft
**Year**: 1992

#### Overview
AVI is one of the oldest video formats still in use. While outdated, it remains compatible with many legacy systems.

#### Pros
- Very widely supported
- Simple structure
- Works on old devices

#### Cons
- No modern codec support
- Large file sizes
- No streaming support
- Limited features

#### Supported Codecs
| Video | Audio |
|-------|-------|
| MPEG-4 | MP3 |
| DivX | AC-3 |
| Xvid | PCM |
| Motion JPEG | |

#### Best For
- Legacy systems
- Old DVD players
- Compatibility with ancient software

---

### MOV (QuickTime)

**Extension**: `.mov`
**Developed by**: Apple
**Year**: 1991

#### Overview
Apple's container format. Excellent for professional video work and Apple ecosystem.

#### Pros
- Excellent Apple support
- Professional editing support
- High-quality codec support
- ProRes support

#### Cons
- Less compatible outside Apple
- Larger files than MP4
- Some codecs are Apple-only

#### Best For
- Apple devices
- Professional video editing
- Final Cut Pro workflows

---

## Video Codecs

Codecs compress and decompress video data.

### H.264 (AVC)

**Full Name**: Advanced Video Coding
**Standard**: MPEG-4 Part 10
**Year**: 2003

#### Overview
H.264 is the most widely used video codec in the world. It powers most internet video, Blu-rays, and broadcast television.

#### Technical Details
| Property | Value |
|----------|-------|
| Compression | Lossy |
| Max Resolution | 8K (Level 6.2) |
| Bit Depth | 8-bit (10-bit with extensions) |
| Color Space | 4:2:0, 4:2:2, 4:4:4 |

#### Quality vs Speed
| Preset | Speed | Quality | Use Case |
|--------|-------|---------|----------|
| ultrafast | ★★★★★ | ★☆☆☆☆ | Real-time streaming |
| fast | ★★★★☆ | ★★★☆☆ | Quick conversions |
| medium | ★★★☆☆ | ★★★★☆ | Balanced (default) |
| slow | ★★☆☆☆ | ★★★★★ | Quality priority |
| veryslow | ★☆☆☆☆ | ★★★★★ | Maximum quality |

#### Pros
- Universal playback support
- Fast encoding
- Mature ecosystem
- Hardware acceleration everywhere

#### Cons
- Licensing fees (built into devices)
- Less efficient than H.265
- Larger files at same quality

#### Best For
- Everything (default choice)
- Maximum compatibility
- Real-time applications

---

### H.265 (HEVC)

**Full Name**: High Efficiency Video Coding
**Year**: 2013

#### Overview
H.265 is the successor to H.264, offering approximately 50% better compression at the same quality level.

#### Technical Details
| Property | Value |
|----------|-------|
| Compression | Lossy |
| Max Resolution | 8K |
| Bit Depth | 8-bit, 10-bit, 12-bit |
| Improvement | ~50% over H.264 |

#### Pros
- Much smaller files
- Excellent quality
- 4K/8K support
- HDR support

#### Cons
- Slower encoding (2-5x)
- Licensing complexity
- Some older devices can't play
- Hardware encoding limited

#### Compatibility
| Device/Platform | Support |
|-----------------|---------|
| iPhone 7+ | Native |
| Android (2017+) | Mostly native |
| Windows 10+ | With extension |
| macOS 10.13+ | Native |
| Smart TVs (2016+) | Usually |

#### Best For
- 4K content
- Long-term archival
- Limited storage
- HDR content

---

### VP9

**Developed by**: Google
**Year**: 2013

#### Overview
Google's open-source, royalty-free answer to H.265. Powers most YouTube 4K video.

#### Technical Details
| Property | Value |
|----------|-------|
| Compression | Lossy |
| License | Royalty-free |
| Max Resolution | 8K |
| Bit Depth | 8-bit, 10-bit, 12-bit |

#### Pros
- Royalty-free
- YouTube native
- Good compression
- Browser support

#### Cons
- Slow encoding
- Limited hardware support
- Less tooling than H.264

#### Best For
- Web video
- YouTube
- Open-source projects

---

### AV1

**Developed by**: Alliance for Open Media
**Year**: 2018

#### Overview
The newest major codec. Even more efficient than H.265/VP9, completely royalty-free.

#### Technical Details
| Property | Value |
|----------|-------|
| Compression | Lossy |
| License | Royalty-free |
| Improvement | ~30% over H.265 |

#### Pros
- Best compression available
- Royalty-free
- Industry backing (Google, Apple, Netflix, etc.)

#### Cons
- Very slow encoding
- Limited hardware support (improving)
- New, less mature

#### Best For
- Future-proofing
- Maximum compression needs

---

## Audio Codecs

### AAC (Advanced Audio Coding)

**Year**: 1997

#### Overview
The modern standard for lossy audio. Better than MP3 at the same bitrate.

| Bitrate | Quality | File Size |
|---------|---------|-----------|
| 96 kbps | Acceptable | Tiny |
| 128 kbps | Good | Small |
| 192 kbps | Very good | Medium |
| 256 kbps | Excellent | Medium |
| 320 kbps | Near-transparent | Larger |

#### Best For
- Modern devices
- Streaming
- Video audio tracks

---

### MP3 (MPEG-1 Audio Layer III)

**Year**: 1993

#### Overview
The universal audio format. Every device supports it.

| Bitrate | Quality |
|---------|---------|
| 128 kbps | Acceptable |
| 192 kbps | Good |
| 256 kbps | Very good |
| 320 kbps | Excellent |

#### Best For
- Maximum compatibility
- Music distribution
- Podcasts

---

### FLAC (Free Lossless Audio Codec)

**Year**: 2001

#### Overview
Lossless compression - perfect quality at ~50% of WAV size.

#### Best For
- Archival
- Audiophiles
- Source files

---

### Opus

**Year**: 2012

#### Overview
The most efficient lossy codec. Excellent at all bitrates.

#### Best For
- Voice communication
- Low-bandwidth streaming
- WebRTC

---

## Compatibility Quick Reference

### Video Format Compatibility

| Format | Windows | macOS | iOS | Android | Web |
|--------|---------|-------|-----|---------|-----|
| MP4 H.264 | ✅ | ✅ | ✅ | ✅ | ✅ |
| MP4 H.265 | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |
| MKV H.264 | ⚠️ | ⚠️ | ❌ | ✅ | ❌ |
| WebM VP9 | ✅ | ⚠️ | ❌ | ✅ | ✅ |
| AVI | ✅ | ⚠️ | ❌ | ⚠️ | ❌ |
| MOV | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |

✅ Native | ⚠️ With app/codec | ❌ Not supported

### Audio Format Compatibility

| Format | Windows | macOS | iOS | Android | Web |
|--------|---------|-------|-----|---------|-----|
| MP3 | ✅ | ✅ | ✅ | ✅ | ✅ |
| AAC/M4A | ✅ | ✅ | ✅ | ✅ | ✅ |
| FLAC | ⚠️ | ⚠️ | ❌ | ✅ | ⚠️ |
| WAV | ✅ | ✅ | ✅ | ✅ | ✅ |
| OGG | ⚠️ | ⚠️ | ❌ | ✅ | ✅ |
| Opus | ⚠️ | ⚠️ | ❌ | ✅ | ✅ |

---

## Choosing the Right Format

### Decision Flowchart

```
What's your priority?

COMPATIBILITY → MP4 + H.264 + AAC
QUALITY → MKV + H.264 + FLAC (or MP4 + H.265)
FILE SIZE → MP4 + H.265 + AAC
WEB → WebM + VP9 + Opus
APPLE → MP4 + H.264 + AAC (or MOV)
ARCHIVAL → MKV + H.264/H.265 + FLAC
```

### By Use Case

| Use Case | Container | Video Codec | Audio Codec |
|----------|-----------|-------------|-------------|
| Share with anyone | MP4 | H.264 | AAC |
| YouTube upload | MP4 | H.264 | AAC |
| Store 4K movies | MKV | H.265 | FLAC/AAC |
| Web embedding | WebM | VP9 | Opus |
| Apple devices | MP4/MOV | H.264 | AAC |
| Archival | MKV | H.264 | FLAC |
| Edit later | MOV/MKV | ProRes/DNxHD | PCM |

---

## Next Steps

- [Video Conversion Guide](video-conversion.md) - Conversion tutorials
- [Audio Conversion Guide](audio-conversion.md) - Audio specifics
- [Troubleshooting](troubleshooting.md) - Fix issues
