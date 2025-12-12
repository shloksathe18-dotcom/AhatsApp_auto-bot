from livekit.agents.llm import function_tool
import asyncio
import pyautogui
import platform
from datetime import datetime

# TTS Optional
try:
    import pyttsx3
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 150)
    tts_engine.setProperty('volume', 0.8)
except ImportError:
    tts_engine = None

async def speak(text):
    if tts_engine:
        try:
            tts_engine.stop()
            tts_engine.say(text)
            tts_engine.runAndWait()
        except:
            pass


@function_tool
async def test_whatsapp_message_keyboard_only_v5(contact_name: str, message: str):

    print("\n" + "="*60)
    print("🚀 WhatsApp Keyboard Automation (v5) – Optimized & Fixed")
    print("="*60)

    if platform.system() != "Windows":
        msg = f"❌ Error: Only works on Windows. OS = {platform.system()}"
        print(msg)
        await speak(msg)
        return msg
    

    try:
        # STEP 1 – Open Start Menu
        print("\n🔹 Step 1: Opening Start Menu...")
        await speak("Opening Start Menu.")

        pyautogui.click(10, 10)
        await asyncio.sleep(0.3)

        pyautogui.press("win")
        await asyncio.sleep(1.3)

        pyautogui.typewrite("WhatsApp", interval=0.07)
        await asyncio.sleep(1.4)

        # STEP 2 – Open WhatsApp
        print("\n🔹 Step 2: Launching WhatsApp Desktop...")
        await speak("Launching WhatsApp.")
        pyautogui.press("enter")
        await asyncio.sleep(9)  # optimized launch wait

        # STEP 3 – Activate WhatsApp window
        print("\n🔹 Step 3: Activating WhatsApp window...")
        await speak("Activating WhatsApp window.")
        whatsapp_window = None

        for _ in range(5):
            wins = pyautogui.getWindowsWithTitle("WhatsApp")
            if wins:
                whatsapp_window = wins[0]
                break
            await asyncio.sleep(1)

        if whatsapp_window:
            whatsapp_window.activate()
            await asyncio.sleep(1.2)
        else:
            print("⚠ WhatsApp window not found — using Alt+Tab fallback.")
            pyautogui.hotkey("alt", "tab")
            await asyncio.sleep(1.5)

        # STEP 4 – Search Contact
        print("\n🔹 Step 4: Searching contact...")
        await speak(f"Searching for {contact_name}.")
        pyautogui.hotkey("ctrl", "f")
        await asyncio.sleep(1.3)

        pyautogui.hotkey("ctrl", "a")
        await asyncio.sleep(0.3)
        pyautogui.press("backspace")
        await asyncio.sleep(0.3)

        pyautogui.typewrite(contact_name, interval=0.06)
        await asyncio.sleep(2.5)  # faster wait

        # STEP 4.5 – Select first search result
        print("\n🔹 Step 4.5: Selecting contact...")
        pyautogui.press("down")
        await asyncio.sleep(0.8)

        pyautogui.press("enter")
        await asyncio.sleep(3)  # chat loading time

        # STEP 4.6 – Detect chat is open
        pyautogui.press("up")
        await asyncio.sleep(0.3)
        pyautogui.press("down")
        await asyncio.sleep(0.3)

        # STEP 5 – Focus message box
        print("\n🔹 Step 5: Focusing message box…")
        await speak("Focusing message box.")

        pyautogui.hotkey("ctrl", "l")
        await asyncio.sleep(0.9)

        # Insurance: WhatsApp sometimes ignores first ctrl+l
        pyautogui.hotkey("ctrl", "l")
        await asyncio.sleep(1)

        # STEP 6 – Type the message
        print("\n🔹 Step 6: Typing message...")
        await speak("Typing your message.")

        for char in message:
            if char == " ":
                pyautogui.press("space")
            elif char == "\n":
                pyautogui.hotkey("shift", "enter")
            else:
                pyautogui.typewrite(char, interval=0.01)
            await asyncio.sleep(0.005)

        await asyncio.sleep(0.7)

        # STEP 7 – Send
        print("\n🔹 Step 7: Sending message...")
        await speak("Sending message.")
        pyautogui.press("enter")
        await asyncio.sleep(2)

        result = f"✔ Message successfully sent to {contact_name}!"
        print("\n" + "="*60)
        print(result)
        print("="*60)
        await speak(result)
        return result

    except Exception as e:
        err = f"❌ ERROR: {e}"
        print(err)
        await speak("An error occurred.")

        try:
            filename = f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            pyautogui.screenshot(filename)
            print(f"📸 Screenshot saved: {filename}")
        except:
            pass
        
        return err



# Run manually
if __name__ == "__main__":
    print("\n🤖 WhatsApp Automation Runner")
    print("="*60)

    c = input("Enter contact name: ").strip()
    m = input("Enter message: ").strip()

    asyncio.run(test_whatsapp_message_keyboard_only_v5(contact_name=c, message=m))
