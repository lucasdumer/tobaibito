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

            if subprocess.check_output('xset q | grep LED', shell=True)[65] == 50 :
                c = False
            if subprocess.check_output('xset q | grep LED', shell=True)[65] == 51 :
                c = True
            print( "c is : ", c)

            if c:

                px = ImageGrab.grab().load()

                print(px[1080, 12])

                m = px[771, 84]
                v = px[926, 82]
                
                print('x pont=', px[x, y])
                print('c pont=', m)

                if m[0] == 46 and m[1] == 46 and m[2] == 46:
                    pyautogui.press("f")
                
                if v[0] == 38 and v[1] == 38 and v[2] == 38:
                    pyautogui.press("num3")

                cp = px[941, 11]
                if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                    pyautogui.press("num7")

                cp = px[951, 11]
                if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                    pyautogui.press("num7")

                cp = px[961, 11]
                if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                    pyautogui.press("num7")

                cp = px[971, 11]
                if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                    pyautogui.press("num7")

        except:
            a = 1
        time.sleep(1)

threading.Thread(target=process).start()
