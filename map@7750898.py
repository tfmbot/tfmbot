import pyautogui # manage mouse movements
import keyboard # manage keyboard 
#map : @7750898

def combo1():
    pyautogui.moveTo(955,221)# Moves Mouse to these coordinates
    keyboard.send("3")# THis presses 3 
    keyboard.send("x") # presses x for rotation clockwise
    pyautogui.dragTo(824,235,duration=1) #this will hold mouse from 955,221 location to 824,235 in 1 second for cannon to spawn
    keyboard.send("2")
    keyboard.send("z")# Rotation of object anticlockwise
    keyboard.send("z")
    pyautogui.dragTo(824,235,duration=1) 
    #now you jsut repeat the same proces and do combos all it changes it coordinates and the use of Rotation (x/z) and cannon 3 2 1 
def combo2():
    pyautogui.moveTo(946,387)
    keyboard.send("1")
    pyautogui.dragTo(978,260,duration=1)
    keyboard.send("3")
    for _ in range(6):
        keyboard.send("x")
    pyautogui.dragTo(758,395,duration=1)
    keyboard.send("3")
    keyboard.send("x")
    keyboard.send("x")
    pyautogui.dragTo(758,407,duration=1) # what im doing here is increasing the Y coordinate which means the cannon is being lowered down3
    keyboard.send("3")
    keyboard.send("x")
    pyautogui.dragTo(758,407,duration=1) 
def combo3():
    pyautogui.moveTo(810,338)
    keyboard.send("1")
    pyautogui.dragTo(825,354,duration=1)
    keyboard.send("1")
    keyboard.send("x")
    pyautogui.dragTo(899,459,duration=1)
    keyboard.send("3")
    keyboard.send("z")
    pyautogui.dragTo(899,459,duration=1)
    
keyboard.add_hotkey("p",combo1) # When Q pressed Runs thee findLocation
keyboard.add_hotkey("o",combo2)
keyboard.add_hotkey("l",combo3)
keyboard.wait("ESC") # Waits for ESC to close the code
