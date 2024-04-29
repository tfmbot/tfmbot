import pyautogui
import keyboard
#map : @7673750
def combo1():
    pyautogui.moveTo(927 , 194)
    keyboard.send("1")
    pyautogui.dragTo(926 , 194,duration=1)
    keyboard.send("3")
    for i in range(6):
        keyboard.send("x")
    pyautogui.dragTo(925 , 194,duration=1)
    keyboard.send("1")
    pyautogui.dragTo(925 , 194,duration=1)
def combo2():
    pyautogui.moveTo(927 , 194)
    keyboard.send("3")
    for i in range(6):
        keyboard.send("x")
    pyautogui.dragTo(847 , 389,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(847 , 389,duration=1)
def combo3():
    pyautogui.moveTo(631 , 407)
    keyboard.send("1")
    pyautogui.dragTo(621 , 417,duration=1)
    keyboard.send("1")
    keyboard.send("z")
    pyautogui.dragTo(602 , 494,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(602 , 494,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")
