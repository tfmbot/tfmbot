import pyautogui
import keyboard
#MAP:  @490248
def cobmo1():
    pyautogui.moveTo(1294 , 231)
    keyboard.send("3")
    for i in range(5):
        keyboard.send("x")
    pyautogui.dragTo(1280 , 238,duration=1)
    keyboard.send("3")
    keyboard.send('x')
    keyboard.send('x')
    keyboard.send('x')
    keyboard.send('x')
    pyautogui.dragTo(1280 , 238,duration=1)
def combo2():
    pyautogui.moveTo(1189 , 240)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1138 , 281,duration=1)
    keyboard.send("3")
    keyboard.send('z')
    pyautogui.dragTo(1138 , 281,duration=1)
def combo3():
    pyautogui.moveTo(1218 , 217)
    keyboard.send("1")
    keyboard.send("x")
    pyautogui.dragTo(1127 , 281,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(1127 , 281,duration=1)
keyboard.add_hotkey("p",cobmo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")

