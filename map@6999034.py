import keyboard
import pyautogui
#map : @6999034
def combo1():
    pyautogui.moveTo(489 , 232)
    keyboard.send("1")
    keyboard.send("z")
    pyautogui.dragTo(530 , 374,duration=.99)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(530 , 374,duration=1)
def combo2():
    pyautogui.moveTo(689 , 278)
    keyboard.send("1")
    keyboard.send("space")
    pyautogui.dragTo(646 , 253,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(712 , 317,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(712 , 317,duration=1)
def combo3():
    pyautogui.moveTo(709 , 240)
    keyboard.send("1")
    keyboard.send("z")
    pyautogui.dragTo(676 , 389,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(757 , 240,duration=1)
    keyboard.send("2")
    for i in range(5):
        keyboard.send("z")
    pyautogui.dragTo(701 , 368,duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(701 , 368,duration=1)
keyboard.add_hotkey("p", combo1)
keyboard.add_hotkey("o", combo2)
keyboard.add_hotkey("l", combo3)
keyboard.wait("ESC")








