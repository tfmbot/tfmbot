import pyautogui
import keyboard
#map : @489470
def combo1():
    pyautogui.moveTo(887 , 357)
    keyboard.send("2")
    pyautogui.dragTo(884 , 370,duration=1)
    keyboard.send("2")
    pyautogui.dragTo(997 , 199,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1001 , 204, duration=1)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(826 , 389, duration=1)
    keyboard.send("3")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(826 , 389, duration=1)

keyboard.add_hotkey("p",combo1)
keyboard.wait("ESC")

