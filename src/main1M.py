import time
import pyautogui, sys
from PIL import ImageGrab
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller, Listener
import threading
import subprocess

keyboard = Controller()

print("start")

e = False
a = False

def process():
    global e
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

                fm = px[1053, 15]
                fmm = px[698, 14]
                nm = px[874, 16]

                print('x pont=', px[x, y])
            
                if fm[0] == 48 and fm[1] == 48 and fm[2] == 48:
                    pyautogui.press("1")

                f = False
                if fmm[0] == 29 and fmm[1] == 29 and fmm[2] == 29:
                    pyautogui.press("2")
                    f = True

                if nm[0] == 34 and nm[1] == 34 and nm[2] == 34 and f == False:
                    pyautogui.press("3")

        except:
            b = 1
        time.sleep(0.5)

threading.Thread(target=process).start()
