import time
import pyautogui, sys
from PIL import ImageGrab
from pynput.keyboard import Key, Controller, Listener
import threading
import mouse

keyboard = Controller()

w = False
a = False
s = False
d = False

print("start")

def on_press(key):
    global w
    global a
    global s
    global d
    try:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        if key.char == '2':
            pyautogui.moveTo(1551, 484)
            pyautogui.rightClick()
            pyautogui.moveTo(991, 490)
            pyautogui.click()
            pyautogui.moveTo(1551, 484)
            pyautogui.dragTo(1551, 425, button='left')
        if key.char == '6':
            x, y = pyautogui.position()
            pyautogui.moveTo(1548, 542)
            pyautogui.rightClick()
            pyautogui.moveTo(x, y)
        if key.char == '5':
            x, y = pyautogui.position()
            pyautogui.moveTo(1550, 603)
            pyautogui.rightClick()
            pyautogui.moveTo(x, y)
        if key.char == 'w':
            w = True
        if key.char == 'a':
            a = True
        if key.char == 's':
            s = True
        if key.char == 'd':
            d = True
        print(w)
        print(a)
        print(s)
        print(d)
    except:
        print("except")

def on_release(key):
    global w
    global a
    global s
    global d
    try:
        if key.char == 'w':
            w = False
        if key.char == 'a':
            a = False
        if key.char == 's':
            s = False
        if key.char == 'd':
            d = False
        print(w)
        print(a)
        print(s)
        print(d)
    except:
        print("except")

with Listener(
    on_press=on_press,
    on_release=on_release
) as listener: listener.join()
