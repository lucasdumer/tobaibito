import time
from computer import Computer

class Bot:
    def __init__(self):
        self.computer = Computer()

    def start(self):
        windows = self.computer.get_windows()
        i = 0
        while True:
            print(i)
            time.sleep(0.51)
            i += 1