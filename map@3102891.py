import pyautogui
import keyboard
#map : @3102891
def combo1():
    pyautogui.moveTo(744 , 228)
    keyboard.send("3")
    for i in range(6):
        keyboard.send("x")
    pyautogui.dragTo(661 , 434,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(621 , 477,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(700 , 477,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(700 , 477,duration=1)
def combo3():
    pyautogui.moveTo(575 , 424) 
    keyboard.send("3")
    keyboard.send("x") 
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(624 , 480,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    pyautogui.dragTo(624 , 480,duration=1)
def combo2():
    pyautogui.moveTo(575 , 449)
    keyboard.send("3")
    for i in range(4):
        keyboard.send("x")
    pyautogui.dragTo(666 , 229,duration=1)
    keyboard.send("1")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(682 , 470,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(682 , 470,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")
