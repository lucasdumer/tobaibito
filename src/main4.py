import time
import pyautogui, sys
from PIL import ImageGrab
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller, Listener
import threading

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

            px = ImageGrab.grab().load()

            print(px[1080, 12])

            m = px[1080, 12]

            print('c pont=', m)

            if m[0] == 34 and m[1] == 35 and m[2] == 34:
                pyautogui.press("f")
            
            cp = px[941, 11]
            if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                pyautogui.press("7")

            cp = px[951, 11]
            if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                pyautogui.press("7")

            cp = px[961, 11]
            if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                pyautogui.press("7")

            cp = px[971, 11]
            if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                pyautogui.press("7")

        except:
            a = 1
        time.sleep(1)

threading.Thread(target=process).start()
