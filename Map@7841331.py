import pyautogui
import keyboard
import time
#MAP: @7682811
while True:
    if keyboard.is_pressed("q"):
        x , y = pyautogui.position()
        print(x, ",", y)
        time.sleep(0.5)
    if keyboard.is_pressed("P"):
        pyautogui.moveTo(626 , 435)
        keyboard.press("1")
        pyautogui.dragTo(702 , 296, duration=1)
        keyboard.press("2")
        pyautogui.dragTo(752 , 373, duration=1)
    if keyboard.is_pressed("O"):
        pyautogui.moveTo(752 , 373)
        keyboard.press("1")
        keyboard.press("X")
        pyautogui.dragTo(725 , 294, duration=1)
        keyboard.press('2')
        pyautogui.dragTo(725 , 304, duration=1)
    if keyboard.is_pressed("L"):
        pyautogui.moveTo(566 , 460)
        keyboard.press("1")
        pyautogui.dragTo(619 , 424, duration=1)
        keyboard.press("2")
        pyautogui.scroll(300)
        pyautogui.scroll(300)
        pyautogui.scroll(300)
        pyautogui.dragTo(580 , 235, duration=1)
    if keyboard.is_pressed("K"):
        pyautogui.moveTo(580,235)
        keyboard.press("1")
        keyboard.press("z")
        pyautogui.dragTo(614 , 472, duration=1)
        keyboard.press("2")
        keyboard.press("X")
        keyboard.press("X")
        time.sleep(0.5)
        pyautogui.dragTo(614 , 472, duration=1)