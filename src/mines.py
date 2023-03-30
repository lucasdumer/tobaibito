import time
import pyautogui, sys
from PIL import ImageGrab
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller, Listener
import threading
import subprocess

keyboard = Controller()

print("start")

def process():
    while True:
        try:
            print("===================================")
            print("start")
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        
            print(positionStr)

            # full screen alienware
            # pyautogui.click(1223, 897)
            # time.sleep(3)

            # pyautogui.click(802, 441)
            # time.sleep(3)

            # pyautogui.click(1172, 434)
            # time.sleep(3)

            # pyautogui.click(799, 810)
            # time.sleep(3)
            
            # pyautogui.click(1170, 806)
            # time.sleep(3)

            # pyautogui.click(1223, 897)
            # time.sleep(3)
            
            # pyautogui.click(2818, 826)
            # time.sleep(2)

            # pyautogui.click(2172, 236)
            # time.sleep(1)

            # pyautogui.click(2626, 234)
            # time.sleep(1)

            # pyautogui.click(2626, 720)
            # time.sleep(1)

            # pyautogui.click(2172, 721)
            # time.sleep(1)

            # pyautogui.click(2818, 826)
            # time.sleep(2)

        except:
            a = 1
        time.sleep(1)

threading.Thread(target=process).start()
