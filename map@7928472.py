import keyboard
import pyautogui
#map : @7928472
def combo1():
    pyautogui.moveTo(1334 , 292) 
    keyboard.send("1")
    pyautogui.dragTo(1527 , 239,duration=1)
    keyboard.send("3")
    keyboard.send('x')
    keyboard.send('x')
    keyboard.send('x')
    pyautogui.dragTo(1277 , 251,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1277 , 251,duration=1)
def combo2():
    pyautogui.moveTo(1450 , 203)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1314 , 399,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1314 , 399,duration=1)
def combo3():
    pyautogui.moveTo(1418 , 353)
    keyboard.send("1")
    pyautogui.dragTo(1337 , 345,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1337 , 345,duration=1)
def combo4():
    pyautogui.moveTo(1474 , 292)
    keyboard.send("3")
    pyautogui.dragTo(1285 , 192,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1285 , 192,duration=1)

keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.add_hotkey("k",combo4)
keyboard.wait("v")






