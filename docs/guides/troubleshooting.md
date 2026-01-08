# Troubleshooting Guide

This guide helps you solve common issues with MONICA and FFmpeg conversions.

---

## Quick Diagnosis

Before diving into specific issues, try these steps:

1. **Check the logs**: Go to "Logs / status" in the main menu
2. **Verify your source file**: Can it play in VLC?
3. **Try a simple conversion**: Test with MP4 (H.264)
4. **Check disk space**: Ensure enough space in `/export`

---

## Installation Issues

### "Python not found" or "pip not found"

**Problem**: Python isn't installed or not in PATH.

**Solution**:

**Windows**:
1. Download Python from python.org
2. During installation, check "Add Python to PATH"
3. Restart your terminal

**Linux**:
```bash
sudo apt install python3 python3-pip  # Debian/Ubuntu
sudo dnf install python3 python3-pip  # Fedora
```

### "No module named 'questionary'"

**Problem**: Dependencies not installed.

**Solution**:
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install questionary colorama requests
```

### FFmpeg Download Fails

**Problem**: Can't download FFmpeg automatically.

**Possible causes**:
- No internet connection
- Firewall blocking
- GitHub rate limiting

**Solution**:

**Manual download (Windows)**:
1. Go to https://github.com/BtbN/FFmpeg-Builds/releases
2. Download `ffmpeg-master-latest-win64-gpl.zip`
3. Extract `ffmpeg.exe` to a `ffmpeg/` folder in your MONICA directory

**Manual download (Linux)**:
```bash
sudo apt install ffmpeg  # Debian/Ubuntu
sudo dnf install ffmpeg  # Fedora
```

Or download static build:
1. Go to https://johnvansickle.com/ffmpeg/
2. Download and extract
3. Move `ffmpeg` to MONICA's `ffmpeg/` folder

### "FFmpeg not found" After Installation

**Problem**: MONICA can't find FFmpeg even though it's installed.

**Solutions**:

1. **Check PATH**:
   ```bash
   ffmpeg -version  # Should show version info
   ```

2. **Local installation**: Place `ffmpeg` (or `ffmpeg.exe`) in a `ffmpeg/` folder inside your MONICA directory.

3. **Restart terminal**: Close and reopen your terminal after installation.

---

## Conversion Errors

### "Conversion failed" / Process Exits Immediately

**Problem**: FFmpeg encounters an error.

**Steps**:
1. Check "Logs / status" for error details
2. Look for the actual error message

**Common causes**:

| Error Message | Cause | Solution |
|---------------|-------|----------|
| "No such file" | Source file moved | Ensure file is in `/import` |
| "Permission denied" | Can't write output | Check `/export` permissions |
| "Invalid data" | Corrupted source | Try different source file |
| "Encoder not found" | Missing codec | Update FFmpeg |

### Conversion Stops Midway

**Problem**: Progress bar stops, conversion hangs.

**Possible causes**:
- Corrupted section in video
- Disk full
- Out of memory

**Solutions**:
1. **Check disk space**: Ensure `/export` has enough room
2. **Try smaller file first**: Test if MONICA works with other files
3. **Check source file**: Play it in VLC, skip to different parts
4. **Reduce quality**: Use a more compressed preset

### "Output file is 0 bytes"

**Problem**: Conversion creates empty file.

**Causes**:
- FFmpeg crashed
- Unsupported codec in source
- Permissions issue

**Solutions**:
1. Check logs for error message
2. Try remuxing first (to identify codec issues)
3. Verify source file plays correctly

---

## Playback Issues

### Converted File Won't Play

**Problem**: Output file doesn't play on target device.

**Diagnosis**:
1. Does it play in VLC? (VLC plays almost anything)
2. What device/app can't play it?

**Common solutions**:

| Device Can't Play | Try This |
|-------------------|----------|
| iPhone/iOS | Convert to MP4 H.264 |
| Old Smart TV | Use MP4 H.264, avoid H.265 |
| Web browser | Use MP4 H.264 or WebM |
| Windows (no codec) | Install K-Lite Codec Pack |

### Audio Missing in Output

**Problem**: Video plays but no sound.

**Causes**:
- Source has no audio track
- Incompatible audio codec
- Audio codec mismatch

**Solutions**:
1. Check source has audio (play in VLC, check audio track)
2. Use a different preset
3. Try remuxing first to isolate issue

### Audio Out of Sync

**Problem**: Audio and video are not synchronized.

**Causes**:
- Variable frame rate (VFR) source
- Corrupted source file
- Incorrect container choice

**Solutions**:

1. **Remux first**: Sometimes fixes sync issues
   ```
   Remux (no re-encode) → Remux to MP4
   ```

2. **Convert VFR to CFR**: MONICA handles this, but very bad VFR may still have issues

3. **Check source**: If source is synced in VLC but output isn't, the conversion process has an issue

### Video Quality Looks Bad

**Problem**: Output looks worse than source.

**Causes**:
- Wrong preset choice
- Source already compressed
- Resolution mismatch

**Solutions**:

1. **Use higher quality preset**: Try "High Quality" options

2. **Don't upscale**: Converting 720p to 1080p doesn't add quality

3. **Check CRF**: Lower CRF = better quality
   - 18-20: High quality
   - 23: Default
   - 28+: Lower quality

4. **Consider source quality**: Can't improve on source

### Colors Look Wrong

**Problem**: Colors appear washed out or different.

**Causes**:
- Color space mismatch
- HDR content on SDR display
- Player issue

**Solutions**:
1. MONICA uses standard color settings (bt709)
2. If source is HDR, output may look different on non-HDR displays
3. Try different media player

---

## File and Folder Issues

### "No files found in /import"

**Problem**: File picker shows nothing.

**Causes**:
- Files not in `/import` folder
- Wrong file extension
- Hidden files

**Solutions**:
1. Verify files are in the correct `import/` folder
2. Check file extensions match the operation (video files for video conversion)
3. Ensure files aren't hidden (Windows: uncheck "Hidden" in properties)

### Can't Find Output File

**Problem**: Conversion completed but can't find file.

**Solution**:
1. Check the `/export` folder
2. Files are named: `<original>_<timestamp>_<format>_converted.<ext>`
3. Sort by date modified to find recent files

### "Permission denied"

**Problem**: Can't read or write files.

**Windows solutions**:
1. Run terminal as Administrator
2. Move MONICA to a different folder (not Program Files)
3. Check folder permissions

**Linux solutions**:
```bash
chmod -R 755 /path/to/monica
```

---

## Performance Issues

### Conversion is Very Slow

**Problem**: Encoding takes forever.

**Normal vs Slow**:
- H.264 "medium": ~30-60 fps (1 hour video in 1-2 hours)
- H.265: ~10-30 fps (2-5x slower than H.264)
- 4K content: Much slower than 1080p

**Speed tips**:
1. Use "fast" or "medium" presets (not "slow")
2. Use H.264 instead of H.265
3. Close other applications
4. Encoding is CPU-intensive - more cores help

### MONICA Uses Too Much CPU

**Problem**: Computer becomes unresponsive during conversion.

**Solutions**:
1. This is normal - encoding is CPU-intensive
2. Encode when you don't need the computer
3. Some tasks can be paused by pressing Ctrl+C (but you'll lose progress)

### Running Out of Disk Space

**Problem**: Disk fills up during conversion.

**Solutions**:
1. Check available space before starting
2. Output files can be larger than input (temporarily)
3. Delete source files after verifying output (not recommended until verified)
4. Use more compressed presets

---

## Reading Log Files

MONICA logs are stored in `/logs/monica.log`.

### Log Format
```
2026-01-08 14:32:10 | INFO     | JOB START: Recipe 'MP4 (H.264)' with 1 file(s)
2026-01-08 14:32:10 | INFO     |   - /path/to/file.mkv
2026-01-08 14:32:10 | INFO     | ITEM START: file.mkv
2026-01-08 14:35:45 | INFO     | ITEM END: file.mkv - SUCCESS
2026-01-08 14:35:45 | INFO     | JOB END: Recipe 'MP4 (H.264)' - SUCCESS
```

### Finding Errors
Look for `ERROR` entries:
```
2026-01-08 14:32:15 | ERROR    | FFmpeg failed: [error message here]
```

### Viewing Logs

**In MONICA**:
1. Select "Logs / status" from main menu
2. Choose "View recent logs"

**Directly**:
- Open `/logs/monica.log` in any text editor

---

## Common Error Messages

### "Invalid data found when processing input"

**Meaning**: Source file is corrupted or unsupported.

**Solutions**:
1. Try playing source in VLC
2. Re-download or re-rip the source
3. Try remuxing first

### "Encoder not found"

**Meaning**: FFmpeg doesn't have the required encoder.

**Solutions**:
1. Update FFmpeg to latest version
2. Use a different preset
3. Re-download FFmpeg

### "Output format not supported"

**Meaning**: Codec/container combination invalid.

**Solution**: Use a different output format.

### "No space left on device"

**Meaning**: Disk is full.

**Solution**: Free up disk space or use a different drive.

---

## Getting More Help

If you can't solve your issue:

1. **Check the logs** - Copy the error message
2. **Note your setup**:
   - Operating system
   - Python version (`python --version`)
   - FFmpeg version (`ffmpeg -version`)
3. **Describe the problem**:
   - What were you trying to do?
   - What happened instead?
   - Can you reproduce it?
4. **Report on GitHub** with all this information

---

## Prevention Tips

1. **Always verify sources** before batch converting
2. **Keep original files** until you've verified conversions
3. **Test with one file** before processing many
4. **Monitor disk space** especially with large files
5. **Check logs periodically** for warnings

---

## Next Steps

- [Getting Started](getting-started.md) - Basic setup
- [Advanced Tips](advanced-tips.md) - Power user features
- [Formats Explained](formats-explained.md) - Format reference
