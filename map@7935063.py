import pyautogui
import keyboard
#MAP: @7935063
def combo1():
    pyautogui.moveTo(1311 , 124)
    keyboard.send("3")
    for i in range(5):
        keyboard.send("x")
    pyautogui.dragTo(1234 , 344,duration=1)
    keyboard.send("3")
    keyboard.send('z')
    pyautogui.dragTo(1346 , 134,duration=1)
    keyboard.send("3")
    keyboard.send('x')
    keyboard.send('x')
    keyboard.send('x')
    keyboard.send('x')
    pyautogui.dragTo(1194 , 200,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1194 , 200,duration=1)
def combo2():
     pyautogui.moveTo(1259 , 113)
     keyboard.send("1")
     keyboard.send("x")
     keyboard.send("x")
     pyautogui.dragTo(1277 , 374, duration=1)
     keyboard.send("3")
     pyautogui.dragTo(1277 , 374, duration=1)
     
def combo3():
    pyautogui.moveTo(1410 , 256)
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(1295 , 150, duration=1.45)
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(1295 , 150, duration=1)
def combo4():
    pyautogui.moveTo(1179 , 246)
    keyboard.send("1")
    pyautogui.dragTo(1194 , 265,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    pyautogui.dragTo(1236 , 337,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1236 , 337,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.add_hotkey("k",combo4)
keyboard.wait("ESC")
