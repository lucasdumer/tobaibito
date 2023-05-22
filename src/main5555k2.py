import time
import pyautogui, sys
from PIL import ImageGrab
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller, Listener
import threading
import subprocess

keyboard = Controller()

print("start")

def on_press(key):
    try:
        if hasattr(key, 'char'):
            if key.char == '0':

                if subprocess.check_output('xset q | grep LED', shell=True)[65] == 51 :
                    pyautogui.click(x=854, y=499, button='right')
                    pyautogui.click(x=854, y=499, button='right')

                    pyautogui.click(x=854, y=430, button='right')
                    pyautogui.click(x=854, y=430, button='right')

                    pyautogui.click(x=854, y=367, button='right')
                    pyautogui.click(x=854, y=367, button='right')

                    pyautogui.click(x=927, y=367, button='right')
                    pyautogui.click(x=927, y=367, button='right')

                    pyautogui.click(x=996, y=367, button='right')
                    pyautogui.click(x=996, y=367, button='right')

                    pyautogui.click(x=996, y=434, button='right')
                    pyautogui.click(x=996, y=434, button='right')

                    pyautogui.click(x=996, y=498, button='right')
                    pyautogui.click(x=996, y=498, button='right')

                    pyautogui.click(x=926, y=497, button='right')
                    pyautogui.click(x=926, y=497, button='right')
    except Exception as e:
        print("ERROR: 0" +str(e))
        a = 1
        with Listener(
            on_press=on_press
        ) as listener: listener.join()
        time.sleep(1)

with Listener(
    on_press=on_press
) as listener: listener.join()
