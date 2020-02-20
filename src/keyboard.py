from pynput.keyboard import Key, Controller
import time

class Keyboard:
    def __init__(self):
        self.keyboard = Controller()

    def f1(self):
        self.keyboard.press(Key.f1)
        self.keyboard.release(Key.f1)

    def f2(self):
        self.keyboard.press(Key.f2)
        self.keyboard.release(Key.f2)
    
    def f3(self):
        self.keyboard.press(Key.f3)
        self.keyboard.release(Key.f3)

    def f4(self):
        self.keyboard.press(Key.f4)
        self.keyboard.release(Key.f4)

    def f5(self):
        self.keyboard.press(Key.f5)
        self.keyboard.release(Key.f5)

    def space(self):
        self.keyboard.press(Key.space)
        self.keyboard.release(Key.space)

    def execute_bot_confirmation_command(self):
        self.keyboard.press(Key.ctrl)
        time.sleep(0.5)
        self.keyboard.press(Key.down)
        self.keyboard.release(Key.down)
        time.sleep(0.5)
        self.keyboard.press(Key.right)
        self.keyboard.release(Key.right)
        time.sleep(0.5)
        self.keyboard.press(Key.up)
        self.keyboard.release(Key.up)
        time.sleep(0.5)
        self.keyboard.press(Key.left)
        self.keyboard.release(Key.left)
        time.sleep(0.5)
        self.keyboard.press(Key.down)
        self.keyboard.release(Key.down)
        self.keyboard.release(Key.ctrl)