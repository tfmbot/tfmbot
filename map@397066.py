import pyautogui
import keyboard
#map :@397066
def combo1():
    pyautogui.moveTo(1369 , 116)
    keyboard.send("1")
    keyboard.send("x")
    pyautogui.dragTo(1375 , 342,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1375 , 346,duration=1)# this last
def combo2():
    pyautogui.moveTo(1423 , 142)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1284 , 235,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1284 , 235,duration=1)
def combo3():
    pyautogui.moveTo(1452 , 136)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1360 , 401,duration=1.353)
    keyboard.send("3")
    pyautogui.dragTo(1360 , 401,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("esc")
