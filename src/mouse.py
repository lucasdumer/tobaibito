import Xlib.display
from keyboard import Keyboard
from pynput import mouse
from pynput.mouse import Button, Controller
from config.environment import Environment

environment = Environment()

def on_click(x, y, button, pressed):
    # if button == Button.left and pressed:
    #     mouse = Controller()
    #     keyboard = Keyboard()
    #     keyboard.f5()
    
    if button == Button.left and pressed and environment.get('toba_bot_off') == '0':
        mouse = Controller()
        keyboard = Keyboard()
        keyboard.f5()

    # Button.left
    # if not pressed:
        # Stop listener
        # return False

# def on_click(x, y, dx, dy):
#     if environment.get('toba_bot_off') == '0':
#         mouse = Controller()
#         keyboard = Keyboard()
#         keyboard.f5()
#         mouse.click(Button.left, 1)

class Mouse:
    def __init__(self):
        self.keyboard = Keyboard()
        # listener = mouse.Listener(on_click=on_click)
        # listener.start()

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