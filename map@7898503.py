import keyboard
import pyautogui
def findLocation():
    x,y = pyautogui.position()
    print(f"{x},{y}")
def combo1():
    pyautogui.moveTo(1342,250)
    keyboard.send("1")
    pyautogui.dragTo(1512,184, duration=.99, button='left')
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1274,247, duration=.99, button='left')
    keyboard.send("3")
    pyautogui.dragTo(1274,247, duration=.99, button='left')
def combo2():
    pyautogui.moveTo(1488,142)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1409,127, duration=.99, button='left')
    keyboard.send("3")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(1333,346, duration=.99, button='left')
    keyboard.send("3")
    pyautogui.dragTo(1333,346, duration=.99, button='left')
def combo3():
    pyautogui.moveTo(1404,304)
    keyboard.send("3")
    for _ in range(6):
        keyboard.send("x")
    pyautogui.dragTo(1314,355, duration=.99, button='left')
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1365,350, duration=.99, button='left')
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1365,350, duration=.99, button='left')
def combo4():
    pyautogui.moveTo(1419,112)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1406,377, duration=1.05, button='left')
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1406,382, duration=.99, button='left')
keyboard.add_hotkey("Q",findLocation)
keyboard.add_hotkey("h",combo1)
keyboard.add_hotkey("j",combo2)
keyboard.add_hotkey("k",combo3)
keyboard.add_hotkey("l",combo4)
keyboard.wait("ESC")

