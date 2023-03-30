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
    jvp = True

    while True:
        try:
            print("===================================")
            print("start")

            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        
            print(positionStr)

            # X:  745 Y:  348
            # (241, 44, 76)
            px = ImageGrab.grab().load()
            print(px[745, 348])
            print(px[1366, 722])
            cd = px[745, 348]
            if cd[0] == 241 and cd[1] == 44 and cd[2] == 76:
                print("Girando em...")
                if deve_jogar:
                    print("jogando...")
                    deve_jogar = False
                    cw = px[1366, 722]
                    if cw[0] == 38 and cw[1] == 47 and cw[2] == 60:
                        print("preto win...")
                        if jvp:
                            pyautogui.click(636, 400) # X:  636 Y:  400 dobra
                        else:
                            pyautogui.click(441, 397) # X:  636 Y:  400 set
                            pyautogui.press('backspace', presses=10)
                            pyautogui.press('0')
                            pyautogui.press('.')
                            pyautogui.press('1')
                            pyautogui.press('0')
                    elif cw[0] == 240 and cw[1] == 44 and cw[2] == 76:
                        print("vermelho win...")
                        if jvp:
                            pyautogui.click(441, 397) # X:  636 Y:  400 set
                            pyautogui.press('backspace', presses=10)
                            pyautogui.press('0')
                            pyautogui.press('.')
                            pyautogui.press('1')
                            pyautogui.press('0')
                        else:
                            pyautogui.click(636, 400) # X:  636 Y:  400 dobra
                    else:
                        print("branco win...")
                        pyautogui.click(636, 400) # X:  636 Y:  400 dobra
                        pyautogui.click(528, 563) # X:  528 Y:  563 aposta
                    
                    if jvp: # preto
                        pyautogui.click(430, 494) # X:  430 Y:  494 vermelho
                        pyautogui.click(528, 563) # X:  528 Y:  563 aposta
                        jvp = False
                    else: # vermelhor
                        pyautogui.click(619, 495) # X:  619 Y:  495 preto
                        pyautogui.click(528, 563) # X:  528 Y:  563 aposta
                        jvp = True
            else:
                deve_jogar = True

        except:
            a = 1
        time.sleep(0.5)

threading.Thread(target=process).start()
