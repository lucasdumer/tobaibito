import time
from computer import Computer
from pixel import Pixel

class Bot:
    def __init__(self):
        self.computer = Computer()

    def start(self):
        windows = self.computer.get_windows()
        mouse = self.computer.get_mouse()
        last_move_time = time.time()
        while True:
            windows[0].observe()
            now = time.time()
            print(now - last_move_time)
            last_move_time = now
            # time.sleep(0.1)
            # mouse.print_info()
            # pixel = Pixel(mouse.get_x(), mouse.get_y())
            # pixel.print_info()
