import keyboard
import pyautogui
#map : @6549805
def combo1():
    pyautogui.moveTo(1470 , 313)
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(1486 , 207,duration=1.45)
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(1486 , 207,duration=1)
def combo2():
    pyautogui.moveTo(1462 , 314)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1517 , 321,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1306 , 387,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(1306 , 387,duration=1)
    
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.wait("ESC")

