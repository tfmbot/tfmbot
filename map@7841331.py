import pyautogui
import keyboard
#MAP: @7841331
def combo1():
        pyautogui.moveTo(626 , 435)
        keyboard.send("1")
        pyautogui.dragTo(702 , 296, duration=1)
        keyboard.send("2")
        pyautogui.dragTo(752 , 373, duration=1)
def combo2():
        pyautogui.moveTo(752 , 373)
        keyboard.send("1")
        keyboard.send("X")
        pyautogui.dragTo(725 , 294, duration=1)
        keyboard.send('2')
        pyautogui.dragTo(725 , 304, duration=1)
def combo3():
        pyautogui.moveTo(566 , 460)
        keyboard.send("1")
        pyautogui.dragTo(619 , 424, duration=1)
        keyboard.send("2")
        keyboard.send("z")
        keyboard.send("z")
        keyboard.send("z")
        pyautogui.dragTo(580 , 235, duration=1)
def combo4():
        pyautogui.moveTo(580,235)
        keyboard.send("1")
        keyboard.send("z")
        pyautogui.dragTo(614 , 472, duration=1.35)
        keyboard.send("2")
        keyboard.send("X")
        pyautogui.dragTo(614 , 472, duration=1)
        
keyboard.add_hotkey("p", combo1)
keyboard.add_hotkey("o", combo2)
keyboard.add_hotkey("l", combo3)
keyboard.add_hotkey("k", combo4)
keyboard.wait("ESC")
