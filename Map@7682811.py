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
        pyautogui.moveTo(569,338)
        keyboard.press("2")
        pyautogui.dragTo(749 , 200, duration=1)
        keyboard.press("2")
        time.sleep(0.39)
        pyautogui.dragTo(577 , 334, duration=1)
        keyboard.press("2")
        pyautogui.moveTo(655 , 248)
        keyboard.press("2")
        pyautogui.dragTo(753 , 214, duration=1)
        keyboard.press("2")
        pyautogui.dragTo(753 , 214, duration=1)
    if keyboard.is_pressed("O"):
        pyautogui.moveTo(740 , 262)
        keyboard.press("1")
        keyboard.press("z")
        pyautogui.dragTo(702 , 444, duration=1)
        keyboard.press("2")
        pyautogui.dragTo(840 , 325, duration=1)
        keyboard.press("1")
        pyautogui.dragTo(797 , 427,duration=1)
        keyboard.press("2")
        keyboard.press("x")
        pyautogui.dragTo(797 , 427,duration=1)