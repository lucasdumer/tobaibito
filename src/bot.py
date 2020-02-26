import time
from computer import Computer
from pixel import Pixel
from config.environment import Environment

environment = Environment()
environment.set('toba_bot_off', '1')
environment.set('toba_bot_on_heal_life_mana', '0')
environment.set('toba_bot_on_heal_mana_utamo', '0')
environment.set('toba_bot_on_heal_mana', '0')

class Bot:
    def __init__(self):
        self.computer = Computer()

    def start(self):
        windows = self.computer.get_windows()
        mouse = self.computer.get_mouse()
        last_move_time = time.time()
        environment = Environment()
        while True:
            if environment.get('toba_bot_off') == '0':
                print("bot on")
                windows[0].observe()
            else:
                print("bot off")
                time.sleep(2)

            # windows[0].observe()

            # now = time.time()
            # print(now - last_move_time)
            # last_move_time = now
            # mouse.print_info()
            # pixel = Pixel(mouse.get_x(), mouse.get_y())
            # pixel.print_info()