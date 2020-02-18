from pynput.keyboard import Key, Controller
from pixel import Pixel
from config.environment import Environment

class Mana:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.environment = Environment()
        incomplete_mana_bar = True
        x_end_bar = self.x
        while incomplete_mana_bar:
            pixel = Pixel(x_end_bar + 1, y)
            if pixel.its_a_pixel_of_mana():
                x_end_bar = x_end_bar + 1
            else:
                incomplete_mana_bar = False
        total_pixel_mana_bar = x_end_bar - self.x
        self.x_pixel_to_heal = self.x + ((total_pixel_mana_bar / 100) * (100 - self.environment.get_auto_potion_mana()))
        self.keyboard = Controller()
    
    def observe(self):
        pixel = Pixel(self.x_pixel_to_heal, self.y)
        if pixel.its_a_pixel_of_mana() == False:
            print("f3")
            self.keyboard.press(Key.f3)
            self.keyboard.release(Key.f3)