import time
import pyautogui, sys
from PIL import ImageGrab
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller, Listener
import threading
import subprocess

keyboard = Controller()

print("start")

x = False

def process():
    global x
    eon = False
    egon = False
    emon = False
    te = 0
    while True:
        eon = False
        egon = False
        emon = False
        try:
            print("===================================")
            print(x)
            if x and subprocess.check_output('xset q | grep LED', shell=True)[65] == 51:
                px = ImageGrab.grab().load()

                e = px[493, 866] # 185 73 20
                eg = px[565, 865] # 167 166 185
                em = px[528, 865] # 138 116 106

                print(e)

                if e[0] == 185 and e[1] == 73 and e[2] == 20:
                    eon = True

                if eon and te < 2:
                    pyautogui.press("Num4")
                    te = te + 1
                    continue

                if em[0] == 138 and em[1] == 116 and em[2] == 106:
                    emon = True

                if emon and te == 1:
                    pyautogui.press("Num5")
                    continue

                if eg[0] == 167 and eg[1] == 166 and eg[2] == 185:
                    egon = True

                if te == 2 and egon:
                    pyautogui.press("Num6")
                    te = 0

        except:
            b = 1
        time.sleep(0.5)

threading.Thread(target=process).start()

def on_press(key):
    global x
    try:
        if hasattr(key, 'char'):
            if key.char == 'x':
                if x:
                    x = False
                else:
                    x = True
    except Exception as e:
        print("ERROR: 0" +str(e))
        a = 1
        with Listener(
            on_press=on_press
        ) as listener: listener.join()

with Listener(
    on_press=on_press
) as listener: listener.join()
