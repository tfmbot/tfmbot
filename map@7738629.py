import keyboard
import pyautogui
#map : @7738629
def combo1():
    pyautogui.moveTo(828 , 407)
    keyboard.send("1")
    keyboard.send("x")
    pyautogui.dragTo(828 , 407,duration=1)
def combo2():
    pyautogui.moveTo(951 , 292)
    keyboard.send("1")
    pyautogui.dragTo(934 , 307,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(1062 , 345,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(1062 , 345,duration=1)
def combo3():
    pyautogui.moveTo(1009 , 287)
    keyboard.send("1")
    pyautogui.dragTo(992 , 306,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1040 , 357,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(1040 , 357,duration=1)
def combo4():
    pyautogui.moveTo(848 , 438)
    keyboard.send("2")
    pyautogui.dragTo(850 , 435,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(850 , 437,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(850 , 437,duration=1)

keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.add_hotkey("k",combo4)
keyboard.wait("ESC")
