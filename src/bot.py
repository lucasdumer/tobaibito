import time
import pyautogui, sys
#from pynput.mouse import Listener
#from pynput.keyboard import Key, Controller

#keyboard = Controller()
#
#def on_click(x, y, button, pressed):
#    print('x=', x, ' y=', y)
#
#with Listener(
#    on_click=on_click
#) as listener: listener.join()

#from computer import Computer
#from pixel import Pixel
#from config.environment import Environment

#environment = Environment()
#environment.set('toba_bot_on', '1')
#environment.set('toba_bot_on_heal_life_mana', '0')
#environment.set('toba_bot_on_heal_mana_utamo', '0')
#environment.set('toba_bot_on_heal_mana', '0')

class Bot:
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
            time.sleep(1)
        #windows = self.computer.get_windows()
        #mouse = self.computer.get_mouse()
        #last_move_time = time.time()
        #environment = Environment()
        #while True:
        #    if environment.get('toba_bot_on') == '0':
        #        print("bot on")
        #        windows[0].observe()
        #    else:
        #        print("bot off")
        #        time.sleep(2)

            # windows[0].observe()

            # now = time.time()
            # print(now - last_move_time)
            # last_move_time = now
            # mouse.print_info()
            # pixel = Pixel(mouse.get_x(), mouse.get_y())
            # pixel.print_info()