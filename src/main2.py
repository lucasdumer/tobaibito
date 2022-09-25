import time
import pyautogui, sys
from PIL import ImageGrab
from pynput.mouse import Listener
from pynput.keyboard import Key, Controller
import threading

keyboard = Controller()

print("bot start")
def process():
    while True:
        print("===================================")
        print("bot loop start")
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)

        px = ImageGrab.grab().load()

        color_mana = px[1013, 20]
        color_vida_mana = px[707, 11]
        print('color_vida_mana=', color_vida_mana)
        if color_vida_mana[0] == 38 and color_vida_mana[1] == 38 and color_vida_mana[2] == 38:
            print('heala vida mana')
            pyautogui.press("num2")
        else:
            print('color_mana=', color_mana)
            if color_mana[0] == 35 and color_mana[1] == 35 and color_mana[2] == 35:
                print('heala mana')
                pyautogui.press("num3")

        color_vida = px[855, 20]
        print('color_vida=', color_vida)
        if color_vida[0] == 41 and color_vida[1] == 41 and color_vida[2] == 41:
            print('heala vida')
            pyautogui.press("num1")
            
        print("===================================")
        time.sleep(1)

threading.Thread(target=process).start()

def on_scroll(x, y, dx, dy):
    if dy > 0:
        keyboard.press('9')
    else:
        keyboard.press('0')
    
with Listener(
    on_scroll=on_scroll
) as listener: listener.join()