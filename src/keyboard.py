from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
from config.environment import Environment

# Key.delete
# Key.home
# Key.end
# Key.page_up
# Key.page_down


def on_press(key):
    environment = Environment()
    if key == Key.delete:
        environment.set('toba_bot_off', '1')
        environment.set('toba_bot_on_heal_life_mana', '0')
        environment.set('toba_bot_on_heal_mana_utamo', '0')
        environment.set('toba_bot_on_heal_mana', '0')
    
    if key == Key.home:
        environment.set('toba_bot_off', '0')
        environment.set('toba_bot_on_heal_life_mana', '1')
        environment.set('toba_bot_on_heal_mana_utamo', '0')
        environment.set('toba_bot_on_heal_mana', '0')

    if key == Key.page_up:
        environment.set('toba_bot_off', '0')
        environment.set('toba_bot_on_heal_life_mana', '0')
        environment.set('toba_bot_on_heal_mana_utamo', '1')
        environment.set('toba_bot_on_heal_mana', '0')

    if key == Key.page_down:
        environment.set('toba_bot_off', '0')
        environment.set('toba_bot_on_heal_life_mana', '0')
        environment.set('toba_bot_on_heal_mana_utamo', '0')
        environment.set('toba_bot_on_heal_mana', '1')

class Keyboard:
    def __init__(self):
        self.keyboard = Controller()
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

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

    def f6(self):
        self.keyboard.press(Key.f6)
        self.keyboard.release(Key.f6)

    def space(self):
        self.keyboard.press(Key.space)
        self.keyboard.release(Key.space)

    def up(self):
        self.keyboard.press(Key.up)
        self.keyboard.release(Key.up)

    def right(self):
        self.keyboard.press(Key.right)
        self.keyboard.release(Key.right)

    def down(self):
        self.keyboard.press(Key.down)
        self.keyboard.release(Key.down)

    def left(self):
        self.keyboard.press(Key.left)
        self.keyboard.release(Key.left)

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