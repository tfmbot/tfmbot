import pyautogui
import keyboard
#MAP:  @4705798
def combo1():
    pyautogui.moveTo(972 , 143)
    keyboard.send("2")
    for i in range(5):
        keyboard.send("z")
    pyautogui.dragTo(892 , 388,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(892 , 388,duration=1)
def combo2():
    pyautogui.moveTo(1001 , 269)
    keyboard.send("1")
    pyautogui.dragTo(990 , 283,duration=1)
    keyboard.send("1")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(892 , 388,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(892 , 388,duration=1)
def combo3():
    pyautogui.moveTo(952 , 138)
    keyboard.send("3")
    for i in range(5):
        keyboard.send('x')
    pyautogui.dragTo(1053 , 375,duration=1)
    keyboard.send("3")
    keyboard.send("z")        
    keyboard.send("z")
    pyautogui.dragTo(1053 , 375,duration=1)
def combo4():
    pyautogui.moveTo(924 , 274)
    keyboard.send("1")
    pyautogui.dragTo(931 , 278,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1053 , 375,duration=1)
    keyboard.send("3")
    keyboard.send("z")        
    keyboard.send("z")
    pyautogui.dragTo(1053 , 375,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.add_hotkey("k",combo4)
keyboard.wait("ESC")









