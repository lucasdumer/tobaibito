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

                fm = px[684, 16]
                fmm = px[900, 14]
                # fmm = ImageGrab.grab(bbox=(900,14,10,10)).load()
                nm = px[1305, 11]
                fmmm = px[900, 21]
                nmm = px[1061, 17]

                print('x pont=', px[x, y])
                print('fmm pont=', fmm)
            
                if fm[0] == 46 and fm[1] == 46 and fm[2] == 46:                    
                    pyautogui.press("1")

                if fmm[0] == 41 and fmm[1] == 41 and fmm[2] == 41:
                    pyautogui.press("3")

                if fmmm[0] == 42 and fmmm[1] == 42 and fmmm[2] == 42 and f == False:
                    pyautogui.press("4")

                if nmm[0] == 42 and nmm[1] == 42 and nmm[2] == 42:
                    pyautogui.press("f")

                if e == False:
                    cp = px[941, 11]
                    if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                        # pyautogui.press("7")
                        pyautogui.press("3")

                    cp = px[951, 11]
                    if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                        # pyautogui.press("7")
                        pyautogui.press("3")

                    cp = px[961, 11]
                    if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                        # pyautogui.press("7")
                        pyautogui.press("3")

                    cp = px[971, 11]
                    if cp[0] == 254 and cp[1] == 0 and cp[2] == 0:
                        # pyautogui.press("7")
                        pyautogui.press("3")
                else:
                    pyautogui.press("5")
        except:
            b = 1
        time.sleep(1)

threading.Thread(target=process).start()

# def c():
#     global a
#     e = True
#     eg = False
#     g = False
#     while True:
#         try:
#             if a:
#                 if e:
#                     pyautogui.press("num4")
#                     pyautogui.press("num4")
#                     pyautogui.press("num4")
#                     e = False
#                     eg = True
#                     time.sleep(2)
#                     continue
#                 if eg:
#                     pyautogui.press("num5")
#                     pyautogui.press("num5")
#                     pyautogui.press("num5")
#                     eg = False
#                     g = True
#                     time.sleep(2)
#                     continue
#                 if g:
#                     pyautogui.press("num6")
#                     pyautogui.press("num6")
#                     pyautogui.press("num6")
#                     g = False
#                     e = True
#                     time.sleep(2)
#                     continue
#         except:
#             b = 1

# threading.Thread(target=c).start()

# def on_press(key):
#     global a
#     try:
#         if hasattr(key, 'char'):
#             if key.char == '`':
#                 if a == True:
#                     a = False
#                 else:
#                     a = True
#     except Exception as e:
#         print("ERROR: " +str(e))
#         b = 1

# with Listener(
#     on_press=on_press
# ) as listener: listener.join()

# def on_press(key):
#     global e
#     try:
#         if hasattr(key, 'char'):
#             if key.char == '`':
#                 if e == True:
#                     e = False
#                 else:
#                     e = True
#     except Exception as e:
#         print("ERROR: 0" +str(e))
#         a = 1
#         with Listener(
#             on_press=on_press
#         ) as listener: listener.join()
#         time.sleep(1)

# with Listener(
#     on_press=on_press
# ) as listener: listener.join()
