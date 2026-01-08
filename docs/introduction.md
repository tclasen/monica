## MONICA: FFmpeg Interactive CLI Tool (Python)

### Goal

Build a **simple, keyboard-driven interactive CLI application** that makes FFmpeg easy to use without exposing FFmpeg syntax.
Target users should not need to manually manage FFmpeg beyond an initial check/download.

---

## Platform & Runtime

* **OS support:** Windows, Linux
* **Language:** Python
* **Entry point:** `main.py`
* **Execution:** `python main.py`
* **FFmpeg handling:**

  * On startup, check if `ffmpeg` is available in PATH
  * If missing:
    * Detect OS
    * Guide user through download OR auto-download once (preferred if feasible, show indicator if available or not in green/red)
  * Never require repeated downloads

---

## Folder Structure (fixed)

```
/import        # input files only
/export        # output files only
/logs          # rolling log file(s)
main.py
requirements.txt
```

* App **only operates on files inside `/import`**
* All outputs go to `/export`

---

## UI / Interaction Model

* **Interactive-only** (no CLI flags)
* **Persistent main menu loop**
* **Keyboard-only navigation**

  * Arrow keys to move
  * Enter to select
* Colored text for clarity (minimal dependency or ANSI)

### Main Menu

```
Convert video
Convert audio
Extract audio
Resize / compress
Short-form content
Remux (no re-encode)
Logs / status
Exit
```

Each menu item opens a submenu if needed.

### Short-form Content Submenu

```
TikTok / Reels (1080x1920)
YouTube Shorts (720x1280)
Instagram / Facebook Stories
Vertical compressed (draft)
───────────────────────────
Crop horizontal to vertical (center)
Letterbox (black bars)
Split screen vertical
Blur background fill
───────────────────────────
TikTok export (≤10 min, 287MB)
Instagram Reels export (≤90 sec)
YouTube Shorts export (≤60 sec)
Snapchat Spotlight export
Facebook Reels export
───────────────────────────
Back to main menu
```

---

## File Selection

* Multi-select from `/import`
* Queue-based execution:
  * One job runs at a time
  * Multiple selections are queued
* Stop immediately on error (no continuation)

---

## Output Naming Convention

Automatically generated, no prompts:

```
<original_name>_<YYYYMMDD_HHMMSS>_<format>_converted
```

Example:

```
video_20260108_143210_mp4_converted.mp4
```

---

## FFmpeg Abstraction

* **Never expose FFmpeg commands or flags**
* All operations defined as **recipes**
* Recipes:
  * Python data structures (or JSON-backed)
  * Map high-level intent → FFmpeg command internally
* Support:
  * Built-in presets
  * User-editable / addable presets (extensible)

---

## Supported Operations (via recipes)

* Video conversion
* Audio conversion
* Audio extraction
* Resize / compress
* Short-form content (vertical video for TikTok, Reels, Shorts)
* Remux (container change, no re-encode)

---

## Progress & Feedback

* Show **progress only** (e.g., percentage bar)
* No raw FFmpeg stderr in UI
* On failure:
  * Stop immediately
  * Log error
  * Return to main menu

---

## Logging

* Rolling log file in `/logs`
* Human-readable text
* Log:
  * Start/end of jobs
  * Selected files
  * Recipe used
  * Errors
  * Warnings
  * Info: Start and End of each item

---

## Dependencies

* **Minimal**
* Only add dependencies if clearly necessary
* All dependencies listed in `requirements.txt`
* Acceptable use cases:
  * Keyboard navigation (arrow keys)
  * Colored output
* Avoid heavy UI frameworks

---

## Extensibility

* Easy to:
  * Add new menu items
  * Add new recipes
  * Edit presets without touching core logic
* Prefer modular functions or small modules, but keep overall structure simple
