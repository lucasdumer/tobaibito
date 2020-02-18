from __future__ import division
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
        self.total_pixel_mana_bar = x_end_bar - self.x
        self.keyboard = Controller()
    
    def observe(self):
        self.x_pixel_to_heal = self.x + ((self.total_pixel_mana_bar / 100) * (100 - self.environment.get_auto_potion_mana()))
        pixel = Pixel(self.x_pixel_to_heal, self.y)
        if pixel.its_a_pixel_of_mana() == False:
            self.keyboard.press(Key.f4)
            self.keyboard.release(Key.f4)