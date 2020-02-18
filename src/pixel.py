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
    
    def equals(self, r, g, b):
        if self.r == r and self.g == g and self.b == b:
            return True
        return False
    
    def its_a_pixel_of_mana(self):
        return self.equals(self.environment.get_mana_r(), self.environment.get_mana_g(), self.environment.get_mana_b())

    def print_info(self):
        print("Pixel:")
        print(self.x, self.y)
        print(self.r, self.g, self.b)