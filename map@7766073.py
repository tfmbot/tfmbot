import pyautogui
import keyboard
#map : @7766073
def combo1():
    pyautogui.moveTo(1205,337) # This will move mouse to that x,y location
    keyboard.send("1") 
    pyautogui.dragTo(1353,314,duration=1) # will hold mouse from last x,y location to the new one so in other word its spawning Cannon
    keyboard.send("2")
    keyboard.send("z")
    pyautogui.dragTo(1223,359,duration=1) #spawning second cannon
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1184,307,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(1184,307,duration=1)
def combo2():
    pyautogui.moveTo(1205,338)
    keyboard.send("1")
    pyautogui.dragTo(1356,322,duration=1)
    keyboard.send("2")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(1226,354,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    keyboard.send("z")
    pyautogui.dragTo(1175,427,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(1175,427,duration=1)
def combo3():
    pyautogui.moveTo(1335,261)
    keyboard.send("1")
    pyautogui.dragTo(1255,460,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(1255,460,duration=1)
keyboard.add_hotkey("p",combo1)
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC")