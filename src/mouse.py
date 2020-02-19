import Xlib.display
from keyboard import Keyboard
from pynput import mouse
from pynput.mouse import Button, Controller

def on_scroll(x, y, dx, dy):
    mouse = Controller()
    keyboard = Keyboard()
    keyboard.f5()
    mouse.click(Button.left, 1)

class Mouse:
    def __init__(self):
        self.keyboard = Keyboard()
        listener = mouse.Listener(on_scroll=on_scroll)
        listener.start()

    def get_x(self):
        data = Xlib.display.Display().screen().root.query_pointer()._data
        return data["root_x"]

    def get_y(self):
        data = Xlib.display.Display().screen().root.query_pointer()._data
        return data["root_y"]
    
    def print_info(self):
        print("Mouse:")
        print("X -> ", self.get_x())
        print("Y -> ", self.get_y())