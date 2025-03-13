import keyboard
import pyautogui
import time
#map : @7667665
try:
    def findLocation():
        x,y = pyautogui.position()
        print(f"{x},{y}")
    def combo1():
        print("TEST")
    
    keyboard.send("Q",findLocation)
    keyboard.wait("ESC")
except:
    print("Closed")

#server down :O