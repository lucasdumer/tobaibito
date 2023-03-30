import time
import pyautogui, sys
from PIL import ImageGrab
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller, Listener
import threading
import subprocess
import random

keyboard = Controller()

print("start")

def process():

    deve_jogar = True
    aposta_v = 8
    aposta_p = 8
    cw = 0
    clearpp = 0
    dvop = True
    evop = True

    d32 = 0
    e32 = 0

    eanv = True
    danv = True

    while True:
        try:
            print("===================================")
            print("start")

            revop = random.randint(1,2)
            rdvop = random.randint(1,2)

            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        
            print(positionStr)

            # X: 1421 Y:  359
            px = ImageGrab.grab().load()
            print(px[x, y])


            xef = 2309
            yef = 335
            # (34, 38, 47)
            # (132, 66, 73)
            # (25, 114, 77)
            print("Finalizou esquerdo: ")
            print(px[xef, yef])
            cef = px[xef, yef]

            xdf = 2708
            ydf = 335
            # (86, 52, 61) verde
            # (126, 61, 69)
            # (28, 34, 43)
            print("Finalizou direita: ")
            print(px[xdf, ydf])
            cdf = px[xdf, ydf]

            if (
                cef[0] == 34 and cef[1] == 38 and cef[2] == 47
            ) or (
                cef[0] == 132 and cef[1] == 66 and cef[2] == 73
            ) or (
                cef[0] == 25 and cef[1] == 114 and cef[2] == 77
            ) or (
                cdf[0] == 86 and cdf[1] == 52 and cdf[2] == 61
            ) or (
                cdf[0] == 126 and cdf[1] == 61 and cdf[2] == 69
            ) or (
                cdf[0] == 28 and cdf[1] == 34 and cdf[2] == 43
            ):
                print("Contador ON!")

                pyautogui.click(2827, 185)
                pyautogui.click(3792, 185)

                xg = 2368
                yg = 389

                cg = px[xg, yg]
                print(cg)
                if cg[0] == 215 and cg[1] == 81 and cg[2] == 86:
                    print("    VERMELHO WIN!!!!")

                    cw = cw + 1

                    if deve_jogar and cw >= 3:
                        print("    JOGANDO!!!!")

                        if eanv:
                            
                            pyautogui.click(2476, 470) #limpa esquerdo
                            pyautogui.click(2361, 470) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_v))
                            time.sleep(0.1)

                        else:

                            pyautogui.click(2662, 470) #aposta 2x
                            

                        if revop == 1:
                            pyautogui.click(2297, 535) #aposta no vermelho agora
                            eanv = True
                        else:
                            pyautogui.click(2735, 535) #aposta no preto agora
                            eanv = False

                        if danv:
                            
                            pyautogui.click(3423, 470) #limpa esquerdo
                            pyautogui.click(3328, 470) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_v))
                            time.sleep(0.1)

                        else:

                            pyautogui.click(3622, 470) #aposta 2x
                            

                        if rdvop == 1:
                            pyautogui.click(3264, 535) #aposta no vermelho agora
                            danv = True
                        else:
                            pyautogui.click(3701, 535) #aposta no preto agora
                            danv = False

                        deve_jogar = False

                elif cg[0] == 19 and cg[1] == 24 and cg[2] == 34:
                    print("    PRETO WIN!!!!")

                    cw = cw + 1

                    if deve_jogar and cw >= 3:
                        print("    JOGANDO!!!!")

                        if eanv:

                            pyautogui.click(2662, 470) #aposta 2x
                            
                        else:

                            pyautogui.click(2476, 470) #limpa esquerdo
                            pyautogui.click(2361, 470) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_v))
                            time.sleep(0.1)
                            
                        if revop == 1:
                            pyautogui.click(2297, 535) #aposta no vermelho agora
                            eanv = True
                        else:
                            pyautogui.click(2735, 535) #aposta no preto agora
                            eanv = False

                        if danv:

                            pyautogui.click(3622, 470) #aposta 2x

                        else:
                            
                            pyautogui.click(3423, 470) #limpa esquerdo
                            pyautogui.click(3328, 470) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_v))
                            time.sleep(0.1)
                            
                        if rdvop == 1:
                            pyautogui.click(3264, 535) #aposta no vermelho agora
                            danv = True
                        else:
                            pyautogui.click(3701, 535) #aposta no preto agora
                            danv = False

                        deve_jogar = False

                else:
                    print("    VERDE WIN!!!!")

                    cw = cw + 1

                    if deve_jogar and cw >= 3:
                        print("    JOGANDO!!!!")

                        pyautogui.click(2662, 470) #aposta 2x
                        pyautogui.click(3622, 470) #aposta 2x

                        if revop == 1:
                            pyautogui.click(2297, 535) #aposta no vermelho agora
                            eanv = True
                        else:
                            pyautogui.click(2735, 535) #aposta no preto agora
                            eanv = False

                        if rdvop == 1:
                            pyautogui.click(3264, 535) #aposta no vermelho agora
                            danv = True
                        else:
                            pyautogui.click(3701, 535) #aposta no preto agora
                            danv = False

                        deve_jogar = False

            else:
                deve_jogar = True
                cw = 0
                

        except:
            a = 1
        time.sleep(0.5)

threading.Thread(target=process).start()
