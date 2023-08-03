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
                    pyautogui.click(x=838, y=520, button='right')
                    pyautogui.click(x=838, y=520, button='right')

                    pyautogui.click(x=838, y=452, button='right')
                    pyautogui.click(x=838, y=452, button='right')

                    pyautogui.click(x=838, y=386, button='right')
                    pyautogui.click(x=838, y=386, button='right')

                    pyautogui.click(x=904, y=386, button='right')
                    pyautogui.click(x=904, y=386, button='right')

                    pyautogui.click(x=972, y=386, button='right')
                    pyautogui.click(x=972, y=386, button='right')

                    pyautogui.click(x=972, y=452, button='right')
                    pyautogui.click(x=972, y=452, button='right')

                    pyautogui.click(x=972, y=530, button='right')
                    pyautogui.click(x=972, y=530, button='right')

                    pyautogui.click(x=904, y=530, button='right')
                    pyautogui.click(x=904, y=530, button='right')
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
