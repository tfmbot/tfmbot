import pyautogui
import keyboard
#map : @479091
def combo1():
    pyautogui.moveTo(615 , 275)
    keyboard.send("1")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(583 , 268,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(583 , 268,duration=1)
def combo2():
    pyautogui.moveTo(533 , 377)
    keyboard.send("2")
    pyautogui.dragTo(533 , 377,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(675 , 245,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(675 , 245,duration=1)
def combo3():
    pyautogui.moveTo(618 , 220)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(613 , 223,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(613 , 223,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")





