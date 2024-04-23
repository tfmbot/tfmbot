import keyboard
import pyautogui
import time
#map : @953515
def combo1():
    pyautogui.moveTo(1047 , 368)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(1130 , 296,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1130 , 296,duration=1)
def combo2():
    pyautogui.moveTo(1149 , 353)
    keyboard.send("3")
    for i in range(6):
        keyboard.send("x")
    pyautogui.dragTo(1129 , 350,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1129 , 350,duration=1)
def combo3():
    pyautogui.moveTo(1146 , 291)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.keyDown("CTRL")
    pyautogui.scroll(300)
    pyautogui.keyUp("CTRL")
    pyautogui.dragTo(1040 , 386,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1040, 386,duration=1)
    
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")




