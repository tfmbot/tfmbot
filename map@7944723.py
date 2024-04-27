import pyautogui
import keyboard
#map : @7944723
def combo1():
    pyautogui.moveTo(800 , 305)
    keyboard.send("1")
    pyautogui.dragTo(786 , 320,duration=1)
    keyboard.send("1")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(832 , 342,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    pyautogui.dragTo(832 , 342,duration=1)
def combo2():
    pyautogui.moveTo(797 , 313)
    keyboard.send("1")
    pyautogui.dragTo(788 , 315,duration=1)
    keyboard.send("1")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(865 , 332,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(861 , 308,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(861 , 308,duration=1)
def combo3():
    pyautogui.moveTo(637 , 343)
    keyboard.send("3")
    for i in range(6):
        keyboard.send("x")
    pyautogui.dragTo(629 , 353,duration=1.1)
    keyboard.send("2")
    pyautogui.dragTo(772 , 441,duration=1.2)
    keyboard.send("2")
    keyboard.send("z")
    pyautogui.dragTo(772 , 441,duration=1)
def combo4():
    pyautogui.moveTo(772 , 358)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(765 , 441,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(765 , 441,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.add_hotkey("k",combo4)
keyboard.wait("ESC")





