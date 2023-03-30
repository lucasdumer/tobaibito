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
            pyautogui.moveTo(1534, 551)
            pyautogui.rightClick()
            if w:
                pyautogui.moveTo(992, 489)
            elif a:
                pyautogui.moveTo(975, 509)
            elif s:
                pyautogui.moveTo(990, 522)
            elif d:
                pyautogui.moveTo(999, 508)
            else:
                pyautogui.moveTo(997, 513)
            pyautogui.click()
        if key.char == '6':
            x, y = pyautogui.position()
            pyautogui.moveTo(1537, 612)
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
