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

            # X: 1421 Y:  359
            px = ImageGrab.grab().load()
            print(px[1611, 358])


            xef = 1395
            yef = 365
            # esquerdo finalizou vermelho
            # X: 1395 Y:  365
            # (38, 42, 53)
            # (136, 70, 79
            # (58, 60, 71)
            print("Finalizou esquerdo: ")
            print(px[xef, yef])
            cef = px[xef, yef]

            xdf = 1733
            ydf = 360
            # X: 1733 Y:  360
            # (19, 109, 73) verde
            # (28, 33, 43)
            # (126, 61, 69)
            # (116, 59, 66)
            print("Finalizou direita: ")
            print(px[xdf, ydf])
            cdf = px[xdf, ydf]

            if (
                cef[0] == 38 and cef[1] == 42 and cef[2] == 53
            ) or (
                cef[0] == 136 and cef[1] == 70 and cef[2] == 79
            ) or (
            #     cef[0] == 58 and cef[1] == 60 and cef[2] == 71
            # ) or (
                cdf[0] == 19 and cdf[1] == 109 and cdf[2] == 73
            ) or (
                cdf[0] == 28 and cdf[1] == 33 and cdf[2] == 43
            ) or (
                cdf[0] == 126 and cdf[1] == 61 and cdf[2] == 69
            ) or (
                cdf[0] == 116 and cdf[1] == 59 and cdf[2] == 66
            ):
                print("Contador ON!")

                xg = 1414
                yg = 405

                cg = px[xg, yg]
                print(cg)
                if cg[0] == 215 and cg[1] == 81 and cg[2] == 86:
                    print("    VERMELHO WIN!!!!")
                    # pyautogui.click(1868, 214)
                    # pyautogui.click(943, 210)
                    # pyautogui.click(2827, 185)
                    # pyautogui.click(3792, 185)
                    cw = cw + 1

                    if deve_jogar and cw >= 3:
                        print("    JOGANDO!!!!")
                        pyautogui.click(1868, 214)
                        pyautogui.click(943, 210)

                        if evop:
                            pyautogui.click(612, 502) #limpa esquerdo
                            pyautogui.click(482, 500) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_v))
                            time.sleep(0.1)
                            pyautogui.click(860, 560) #aposta no preto agora
                            e32 = 0

                            # if d32 < 3:
                            pyautogui.click(1721, 500) #aposta 2x
                            pyautogui.click(1371, 558) #aposta no lado direito no vermelho
                            #     d32 = d32 + 1
                            # else:
                            #     pyautogui.click(1535, 500) #limpa direita
                            #     pyautogui.click(1425, 500) #seleciona caixa de aposta
                            #     pyautogui.press(str(aposta_p))
                            #     time.sleep(0.1)
                            #     pyautogui.click(1371, 558) #aposta no lado direito no vermelho
                            #     d32 = 0

                            evop = False
                            dvop= True

                        else:

                            pyautogui.click(1535, 500) #limpa direita
                            pyautogui.click(1425, 500) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_p))
                            time.sleep(0.1)
                            pyautogui.click(1784, 558) #aposta no preto agora
                            d32 = 0

                            # if e32 < 3:
                            pyautogui.click(797, 500) #aposta 2x
                            pyautogui.click(445, 558) #aposta do lado esquerdo no vermelho
                            #     e32 = e32 + 1
                            # else:
                            #     pyautogui.click(612, 502) #limpa esquerdo
                            #     pyautogui.click(482, 500) #seleciona caixa de aposta
                            #     pyautogui.press(str(aposta_v))
                            #     time.sleep(0.1)
                            #     pyautogui.click(445, 558) #aposta do lado esquerdo no vermelho
                            #     e32 = 0

                            evop = True
                            dvop= False

                        deve_jogar = False

                elif cg[0] == 19 and cg[1] == 24 and cg[2] == 34:
                    print("    PRETO WIN!!!!")

                    cw = cw + 1

                    if deve_jogar and cw >= 3:
                        print("    JOGANDO!!!!")
                        pyautogui.click(1868, 214)
                        pyautogui.click(943, 210)

                        if dvop:
                            pyautogui.click(612, 502) #limpa esquerdo
                            pyautogui.click(482, 500) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_v))
                            time.sleep(0.1)
                            pyautogui.click(449, 560) #aposta no vermelho agora
                            e32 = 0

                            # if d32 < 3:
                            pyautogui.click(1721, 500) #aposta 2x
                            pyautogui.click(1787, 558) #aposta no lado direito no preto
                            #     d32 = d32 + 1
                            # else:
                            #     pyautogui.click(1535, 500) #limpa direita
                            #     pyautogui.click(1425, 500) #seleciona caixa de aposta
                            #     pyautogui.press(str(aposta_p))
                            #     time.sleep(0.1)
                            #     pyautogui.click(1787, 558) #aposta no lado direito no preto
                            #     d32 = 0

                            dvop = False
                            evop = True
                        else:

                            pyautogui.click(1535, 500) #limpa direita
                            pyautogui.click(1425, 500) #seleciona caixa de aposta
                            pyautogui.press(str(aposta_p))
                            time.sleep(0.1)
                            pyautogui.click(1374, 558) #aposta no vermelho agora
                            d32 = 0

                            # if e32 < 3:
                            pyautogui.click(797, 500) #aposta 2x
                            pyautogui.click(865, 558) #aposta do lado esquerdo no preto
                            #     e32 = e32 + 1
                            # else:
                            #     pyautogui.click(612, 502) #limpa esquerdo
                            #     pyautogui.click(482, 500) #seleciona caixa de aposta
                            #     pyautogui.press(str(aposta_v))
                            #     time.sleep(0.1)
                            #     pyautogui.click(865, 558) #aposta do lado esquerdo no preto
                            #     e32 = 0

                            dvop = True
                            evop = False

                        deve_jogar = False

                else:
                    print("    VERDE WIN!!!!")
                    # pyautogui.click(1868, 214)
                    # pyautogui.click(943, 210)
                    cw = cw + 1

                    if deve_jogar and cw >= 4:
                        print("    JOGANDO!!!!")
                        time.sleep(0.1)
                        pyautogui.click(1721, 500) #aposta 2x
                        pyautogui.click(1784, 558) #aposta
                        time.sleep(0.1)
                        pyautogui.click(797, 500) #aposta 2x
                        pyautogui.click(445, 558) #aposta
                        
                        evop = True
                        dvop= False

                        deve_jogar = False

            else:
                deve_jogar = True
                cw = 0
                # clearpp = clearpp + 1
                # if clearpp > 400:
                #     pyautogui.click(1868, 214)
                #     pyautogui.click(943, 210)
                #     time.sleep(1)
                #     pyautogui.click(1868, 214)
                #     pyautogui.click(943, 210)
                #     time.sleep(1)
                #     pyautogui.click(1868, 214)
                #     pyautogui.click(943, 210)
                #     clearpp = 0
                

        except:
            a = 1
        time.sleep(0.5)

threading.Thread(target=process).start()
