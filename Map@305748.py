import pyautogui
import keyboard
import time
#MAP: @305748
while True:
    if keyboard.is_pressed("q"):
        x , y = pyautogui.position()
        print(x, ",", y)
        time.sleep(0.5)
    if keyboard.is_pressed("P"):
        pyautogui.moveTo(935,310)
        keyboard.press("1")
        pyautogui.dragTo(945,314,duration=1)
        keyboard.press("3")
        keyboard.press("x")
        keyboard.press("x")
        pyautogui.dragTo(1034 , 195,duration=1)
        keyboard.press("3")
        pyautogui.scroll(300)
        pyautogui.scroll(300)
        pyautogui.dragTo(962 , 190,duration=1)
    if keyboard.is_pressed("O"):
        pyautogui.moveTo(962 , 190)
        keyboard.press("1")
        keyboard.press("X")
        pyautogui.dragTo(897 , 381, duration=1)
        keyboard.press("3")
        keyboard.press("X")
        keyboard.press("X")
        pyautogui.dragTo(897 , 381, duration=1)
    if keyboard.is_pressed("L"):
        pyautogui.moveTo(966 , 203)
        keyboard.press("1")
        keyboard.press("X")
        pyautogui.dragTo(930 , 387, duration=1)
        keyboard.press("3")
        keyboard.press("X")
        keyboard.press("X")
        pyautogui.dragTo(930 , 387, duration=1)
    if keyboard.is_pressed("K"):
        pyautogui.moveTo(949 , 191)
        keyboard.press("3")
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.dragTo(882 , 389, duration=1)
        keyboard.press("3")
        pyautogui.dragTo(882 , 389, duration=1)
    if keyboard.is_pressed("J"):
        pyautogui.moveTo(974 , 189)
        keyboard.press("3")
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.dragTo(974 , 189, duration=1)