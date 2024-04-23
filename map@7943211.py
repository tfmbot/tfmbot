#map : @7943211
import pyautogui
import keyboard
def combo1():
    pyautogui.moveTo(460 , 277)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(714 , 235, duration=1.1)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(613 , 141, duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(613 , 141, duration=1)
def combo2():
    pyautogui.moveTo(444 , 292)
    keyboard.send("1")
    keyboard.send("z")
    pyautogui.dragTo(490 , 357, duration=1)
    keyboard.send("2")
    pyautogui.dragTo(490 , 357, duration=1)
def combo3():
    pyautogui.moveTo(629 , 335)
    keyboard.send("1")
    pyautogui.dragTo(682 , 368, duration=1)
    keyboard.send("2")
    keyboard.send("x")
    pyautogui.dragTo(559 , 396, duration=1)
    keyboard.send("2")
    pyautogui.dragTo(559 , 396, duration=1)

keyboard.add_hotkey("P", combo1)
keyboard.add_hotkey("O", combo2)
keyboard.add_hotkey("l", combo3)
keyboard.wait("ESC")


