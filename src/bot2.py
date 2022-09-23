import time
import pyautogui, sys
from PIL import ImageGrab

class Bot2:
    def __init__(self):
        print("bot build")
        #self.computer = Computer()

    def start(self):
        print("bot start")
        while True:
            print("bot loop start")
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr)

            px = ImageGrab.grab().load()
            color_mana = px[1013, 20]
            print('color_mana=', color_mana)
            if color_mana[0] == 35 and color_mana[1] == 35 and color_mana[2] == 35:
                print('heala mana')
                pyautogui.press("num3")

            time.sleep(1)