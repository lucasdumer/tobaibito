import time
import pyautogui, sys
from PIL import ImageGrab
from pynput.mouse import Listener
# from pynput.keyboard import Key, Controller, Listener
import threading
import subprocess

# keyboard = Controller()

print("start")

def on_click(x, y, button, pressed):
    print("aaaaa")
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr)
    px = ImageGrab.grab().load()
    print('x pont=', px[x, y])

with Listener(
    on_click=on_click
) as listener: listener.join()

print("start3")
