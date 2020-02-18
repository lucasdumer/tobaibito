import time
from computer import Computer
from pixel import Pixel

class Bot:
    def __init__(self):
        self.computer = Computer()

    def start(self):
        windows = self.computer.get_windows()
        mouse = self.computer.get_mouse()
        i = 0
        while True:
            print(i)
            mouse.print_info()
            pixel = Pixel(mouse.get_x(), mouse.get_y())
            time.sleep(0.51)
            i += 1