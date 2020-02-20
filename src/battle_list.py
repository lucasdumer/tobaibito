from pixel import Pixel
from keyboard import Keyboard

class Battle_list:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.keyboard = Keyboard()
    
    def observe(self):
        pixel = Pixel(self.x, self.y)
        # pixel.print_info()
        pixel2 = Pixel(966, 98)
        # pixel2.print_info()
        if pixel.its_a_pixel_of_live_in_battle_list and pixel2.its_not_a_pixel_atk_target() == False:
            self.keyboard.space()