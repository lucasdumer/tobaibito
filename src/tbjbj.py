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

    deve_jogar = True
    aposta_v = 4
    aposta_p = 4
    cw = 0
    clearpp = 0
    dvop = True
    evop = True

    d32 = 0
    e32 = 0

    opcao = 1
    opcao_loop = 0
    opcao_loop_max = 4

    while True:
        try:
            print("===================================")
            print("start")

            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        
            print(positionStr)

            px = ImageGrab.grab().load()

            print(px[x, y])

            # pyautogui.click(955, 710)

            print(px[665, 539])
            print(px[665, 535])

            # perdeu
            # 872 488
            # (57, 32, 31)

        except:
            a = 1
        time.sleep(0.5)

threading.Thread(target=process).start()
