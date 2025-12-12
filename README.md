# AhatsApp_auto-bot

A small, open-source utility that automates sending WhatsApp Desktop messages using keyboard and mouse events from Python. The script is optimized for Windows and uses `pyautogui` for GUI automation. It also includes optional TTS (text-to-speech) feedback and a `function_tool` decorator to integrate with livekit agent workflows.

**Warning:** This tool controls your mouse and keyboard. Use with caution and never use it to send spam or violate WhatsApp terms of service.

**Intended Use:** This project is provided for educational and fun purposes. It's intended for learning, experimentation, and personal automation. Do not use it for unsolicited messaging or activities that violate WhatsApp Terms of Service or local laws.

**Key features:**
- Keyboard-only automation (no direct WhatsApp API required)
- Sound notifications via `pyttsx3` (optional)
- Designed for Windows 10/11
- Includes helpful delays and fallbacks for window activation and search

**Files:**
- `WhatsApp_auto-bot.py`: Main script with the `test_whatsapp_message_keyboard_only_v5` function and CLI runner.

**Prerequisites**
- Windows 10 or 11 (automation relies on Start menu and keyboard shortcuts)
- Python 3.10+ (or similar)
- WhatsApp Desktop installed and accessible from the Start menu
- (Optional) Microphone/speakers for TTS (if you want audible feedback)

**Recommended Python packages**
You can install dependencies via pip. If you don't use TTS, `pyttsx3` is optional.

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install pyautogui pygetwindow pillow pyttsx3
# If using LiveKit functions integration, install the LiveKit Python package
pip install livekit-agents  # or read LiveKit docs for the correct package
```

**Usage - CLI**
Run the script and follow prompts to input a contact and message:

```bash
python WhatsApp_auto-bot.py
```

When running as a script, you'll be prompted for a contact name and message, and the script will attempt to open WhatsApp, search the contact, focus the message box and send the message.

**Usage - Programmatic**
Import and call the exported `test_whatsapp_message_keyboard_only_v5` coroutine from other Python code or integrate it with an async agent framework such as LiveKit.

Example:

```python
import asyncio
from WhatsApp_auto-bot import test_whatsapp_message_keyboard_only_v5

asyncio.run(test_whatsapp_message_keyboard_only_v5(contact_name='SHLOK', message='Hello!'))
```

**Notes & Troubleshooting**
- The script assumes the WhatsApp window is named "WhatsApp" as returned by `pyautogui.getWindowsWithTitle`.
- Coordinates and timing may vary across machines — adjust `asyncio.sleep()` durations if WhatsApp is slower or faster to respond.
- If the script doesn't activate the correct window, try starting WhatsApp manually first and re-run.
- If `pyttsx3` isn't installed, TTS calls are skipped.
- Because this controls the keyboard and mouse, keep your workstation idle while running.

**Safety and Terms**
Automating messaging to send unsolicited or bulk messages may violate WhatsApp's Terms of Service. Use this script responsibly and only for personal automation or legitimate purposes.

**Contributing**
If you find an issue or would like to add features, please open an issue or PR. Keep changes minimal and test under Windows.

**License**
This project is open source and released under the MIT License — see the LICENSE file for details.

**Credits**
- **Author:** Shlok — the maintainer and original author of this project.
- **Repository:** https://github.com/shloksathe18-dotcom/AhatsApp_auto-bot


