import pyautogui
import keyboard
#map : @741041
def combo1():
    pyautogui.moveTo(1030 , 382)
    keyboard.send("1")
    pyautogui.dragTo(1030 , 382,duration=1)
def combo2():
    pyautogui.moveTo(856 , 267)
    keyboard.send("1")
    pyautogui.dragTo(930 , 186,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    pyautogui.dragTo(1073 , 359,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1073 , 359,duration=1)
def combo3():
    pyautogui.moveTo(829 , 200)
    keyboard.send("3")
    for i in range(6):
        keyboard.send("x")
    pyautogui.dragTo(966 , 396,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(966 , 396,duration=1)
def combo4():
    pyautogui.moveTo(876 , 278)
    keyboard.send("1")
    pyautogui.dragTo(899 , 288,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(838 , 332,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(838 , 332,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.add_hotkey("k",combo4)
keyboard.wait("ESC")
