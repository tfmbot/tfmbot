import pyautogui
import keyboard
import time
#MAP: @7770300
while True:
    if  keyboard.is_pressed("p"):
        pyautogui.moveTo(1485 , 310)
        keyboard.press("3")
        pyautogui.dragTo(1356 , 229, duration=1)
        keyboard.press("3")
        pyautogui.dragTo(1317 , 300,duration=1)
    if keyboard.is_pressed("o"):
        pyautogui.moveTo(1317 , 300)
        keyboard.press("1")
        keyboard.press("SPACE")
        pyautogui.dragTo(1358 , 281, duration=0.98)
        keyboard.press("3")
        keyboard.press("X")
        keyboard.press("X")
        pyautogui.dragTo(1293 , 228, duration=0.98)
        keyboard.press("3")
        pyautogui.dragTo(1293 , 228, duration=0.98)
    if keyboard.is_pressed("l"):
        pyautogui.moveTo(1446 , 200)
        keyboard.press("3")
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.dragTo(1306 , 405, duration=1)
        keyboard.press("3")
        time.sleep(0.1)
        pyautogui.dragTo(1306 , 405,duration=1)
    if keyboard.is_pressed("k"):
        pyautogui.moveTo(1448,201)
        keyboard.press("3")
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.scroll(-300)
        pyautogui.dragTo(1286,244,duration=0.98)
        keyboard.press("3")
        keyboard.press("z")
        time.sleep(0.29)
        pyautogui.dragTo(1286,244,duration=0.98)