import pyautogui
import keyboard
#map : @7003107
def combo1():
    pyautogui.moveTo(1240 , 121)
    keyboard.send("1")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1184 , 136,duration=1)
    keyboard.send("3")
    for i in range(5):
        keyboard.send("x")
    pyautogui.dragTo(1122 , 288,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1122 , 288,duration=1)
def combo2():
    pyautogui.moveTo(1326 , 308)
    keyboard.send("3")
    pyautogui.dragTo(1120 , 240,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(1120 , 240,duration=1)
def combo3():
    pyautogui.moveTo(742 , 425)
    keyboard.send("1")
    pyautogui.dragTo(727 , 437,duration=1)
    keyboard.send("1")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(807 , 413,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(807 , 413,duration=1)

keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")