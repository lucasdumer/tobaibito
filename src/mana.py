from __future__ import division
from keyboard import Keyboard
from pixel import Pixel
from config.environment import Environment
import time

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
        self.keyboard = Keyboard()
        self.last_shild = 0
    
    def observe(self):
        self.x_pixel_to_heal = self.x + ((self.total_pixel_mana_bar / 100) * (100 - self.environment.get_auto_potion_mana()))
        pixel = Pixel(self.x_pixel_to_heal, self.y)
        if pixel.its_a_pixel_of_mana() == False:
            self.keyboard.f4()
    
    def observe_shild(self):
        now = time.time()
        if now - self.last_shild > 60:
            self.keyboard.f6()
            self.last_shild = now