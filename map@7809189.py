#map : @7809189
import pyautogui
import keyboard
def combo1():
    pyautogui.moveTo(1399 , 408)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1254 , 346, duration=1.1)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1233, 346, duration=1)
def combo2():
    pyautogui.moveTo(1356 , 273)
    keyboard.send("3")
    pyautogui.dragTo(1333 , 471, duration=1)
    keyboard.send("1")
    pyautogui.dragTo(1270 , 496, duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1270 , 496, duration=1)
def combo3():
    pyautogui.moveTo(1415 , 418)
    keyboard.send("3")
    pyautogui.dragTo(1252 , 254,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1252 , 254,duration=1)
keyboard.add_hotkey("P", combo1)
keyboard.add_hotkey("O", combo2)
keyboard.add_hotkey("L", combo3)
keyboard.wait("ESC")
