import Xlib.display
import PIL.Image
import PIL.ImageStat
from config.environment import Environment

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.environment = Environment()
        o_x_root = Xlib.display.Display().screen().root
        o_x_image = o_x_root.get_image(self.x, self.y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
        o_pil_image_rgb = PIL.Image.frombytes("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
        lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
        rgb = tuple(map(int, lf_colour))
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
    
    def equal(self, another_pixel):
        return self.equalRGB(another_pixel.r, another_pixel.g, another_pixel.b)

    def equalRGB(self, r, g, b):
        return self.r == r and self.g == g and self.b == b
    
    def its_a_pixel_of_life(self):
        dark = self.equalRGB(179, 133, 133)
        red = self.equalRGB(225, 133, 133)
        red2 = self.equalRGB(225, 156, 156)
        yellow = self.equalRGB(230, 207, 137)
        ok1 = self.equalRGB(186, 210, 135)
        full = self.equalRGB(133, 225, 133)
        if dark or red or red2 or yellow or ok1 or full:
            return True
        else:
            return False

    def its_a_pixel_of_mana(self):
        return self.equalRGB(self.environment.get_mana_r(), self.environment.get_mana_g(), self.environment.get_mana_b())
    
    def its_a_pixel_of_live_in_battle_list(self):
        return self.equalRGB(0, 192, 0)

    def its_a_pixel_atk_target(self):
        return self.equalRGB(255, 0, 0)

    def print_info(self):
        print("Pixel:")
        print(self.x, self.y)
        print(self.r, self.g, self.b)