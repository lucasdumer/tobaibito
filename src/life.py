from __future__ import division
from keyboard import Keyboard
from pixel import Pixel
from config.environment import Environment

class Life:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.environment = Environment()
        incomplete_life_bar = True
        x_end_bar = self.x
        while incomplete_life_bar:
            pixel = Pixel(x_end_bar + 1, y)
            if pixel.its_a_pixel_of_life():
                x_end_bar = x_end_bar + 1
            else:
                incomplete_life_bar = False
        self.total_pixel_life_bar = x_end_bar - self.x
        self.keyboard = Keyboard()
    
    def observe(self):
        self.x_pixel_to_heal_strong = self.x + ((self.total_pixel_life_bar / 100) * (self.environment.get_auto_heal_strong()))
        pixel = Pixel(self.x_pixel_to_heal_strong, self.y)
        if pixel.its_a_pixel_of_life() == False:
            self.keyboard.f3()
        else:
            self.x_pixel_to_heal_medium = self.x + ((self.total_pixel_life_bar / 100) * (self.environment.get_auto_heal_medium()))
            pixel = Pixel(self.x_pixel_to_heal_medium, self.y)
            if pixel.its_a_pixel_of_life() == False:
                self.keyboard.f2()
            else:
                self.x_pixel_to_heal_low = self.x + ((self.total_pixel_life_bar / 100) * (self.environment.get_auto_heal_low()))
                pixel = Pixel(self.x_pixel_to_heal_low, self.y)
                if pixel.its_a_pixel_of_life() == False:
                    self.keyboard.f1()