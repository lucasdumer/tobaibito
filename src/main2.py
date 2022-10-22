import time
import pyautogui, sys
from PIL import ImageGrab
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller, Listener
import threading

keyboard = Controller()

rune = 0
log_cura = False
log = False
ctrl = False
log_release = False
log_press = False
wallpaper = True
wpx = 0
wpy = True
print("start")

def process():
    while True:
        try:
            global rune
            global wallpaper
            global wpx
            global wpy
            if log:
                print("===================================")
                print("start")
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            if log:
                print(positionStr)

            px = ImageGrab.grab().load()

            color_mana = px[x, y]
            if log:
                print('cor ponteiro=', color_mana)
            color_mana = px[1061, 17]
            color_vida_mana = px[707, 11]
            if log:
                print('c_v_m=', color_vida_mana)
            if color_vida_mana[0] == 38 and color_vida_mana[1] == 38 and color_vida_mana[2] == 38:
                if log:
                    print('h v m')
                pyautogui.press("num2")
            else:
                if rune > 0:
                    keyboard.press('6')
                    rune = rune - 1
                else:
                    if log:
                        print('c_m=', color_mana)
                    if color_mana[0] == 40 and color_mana[1] == 40 and color_mana[2] == 39:
                        if log:
                            print('h m')
                        pyautogui.press("num3")
            
            cor_para_1 = px[941, 11]
            if cor_para_1[0] == 254 and cor_para_1[1] == 0 and cor_para_1[2] == 0:
                if log_cura:
                    print('tira para 1')
                pyautogui.press("num7")

            cor_para_2 = px[951, 11]
            if cor_para_2[0] == 254 and cor_para_2[1] == 0 and cor_para_2[2] == 0:
                if log_cura:
                    print('tira para 2')
                pyautogui.press("num7")

            cor_para_3 = px[961, 11]
            if cor_para_3[0] == 254 and cor_para_3[1] == 0 and cor_para_3[2] == 0:
                if log_cura:
                    print('tira para 3')
                pyautogui.press("num7")

            cor_para_4 = px[971, 11]
            if cor_para_4[0] == 254 and cor_para_4[1] == 0 and cor_para_4[2] == 0:
                if log_cura:
                    print('tira para 4')
                pyautogui.press("num7")

            color_vida = px[855, 20]
            if log_cura:
                print('c v=', color_vida)
            if color_vida[0] == 41 and color_vida[1] == 41 and color_vida[2] == 41:
                if log_cura:
                    print('h v')
                pyautogui.press("num1")

            if log:
                print("===================================")
            
            if wallpaper:
                if wpy:
                    wpx = wpx + 1
                else:
                    wpx = wpx - 1
                if wpx > 10:
                    wpy = False
                if wpx < 1:
                    wpy = True
                print(wpx * ' ', '*')

            time.sleep(1)
        except:
            a = 1

threading.Thread(target=process).start()

def on_scroll(x, y, dx, dy):
    if dy > 0:
        keyboard.press('9')
    else:
        keyboard.press('0')

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

#with Listener(
#    on_scroll=on_scroll
#    on_click=on_click
#) as listener: listener.join()

def on_press(key):
    global rune
    global ctrl
    global log_press
    try:
        if key.ctrl_l:
            ctrl = True
        if key.char == '6' and ctrl == False:
            if rune == 0:
                rune = 2
    except:
        a = 1
    if log_press:
        print("ctrl=", ctrl)

def on_release(key):
    global ctrl
    global log_release
    try:
        if key.ctrl_l:
            ctrl = False
    except:
        a = 1
    if log_release:
        print("ctrl=", ctrl)

with Listener(
    on_press=on_press,
    on_release=on_release
) as listener: listener.join()
