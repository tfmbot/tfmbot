import pyautogui
import keyboard
#MAP: @7682811
def combo1():
        pyautogui.moveTo(569,338)
        keyboard.send("2")
        pyautogui.dragTo(749 , 200, duration=1.39)
        keyboard.send("2")
        pyautogui.dragTo(577 , 334, duration=1)
        keyboard.send("2")
        pyautogui.dragTo(655 , 248,duration=1)
        keyboard.send("2")
        pyautogui.dragTo(753 , 206, duration=1)
        keyboard.send("2")
        pyautogui.dragTo(753 , 206, duration=1)
def combo2():
        pyautogui.moveTo(740 , 262)
        keyboard.send("1")
        keyboard.send("z")
        pyautogui.dragTo(702 , 444, duration=1)
        keyboard.send("2")
        pyautogui.dragTo(840 , 325, duration=1)
        keyboard.send("1")
        pyautogui.dragTo(797 , 427,duration=1)
        keyboard.send("2")
        keyboard.send("x")
        pyautogui.dragTo(797 , 427,duration=1)


keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.wait("ESC")
