import pyautogui
import keyboard
#map : @236646
def combo1(): 
    pyautogui.moveTo(1186 , 306)
    keyboard.send("1")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1191 , 291,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1191 , 291,duration=1)
def combo2():
    pyautogui.moveTo(1196 , 308)
    keyboard.send("1")
    pyautogui.dragTo(1215 , 324,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1150 , 270,duration=1)
    keyboard.send("3")
    pyautogui.dragTo(1150 , 270,duration=1)
def combo3():
    pyautogui.moveTo(1275 , 201)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1266 , 441,duration=1.1)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1266 , 441,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")







