import Xlib.display
import PIL.Image
import PIL.ImageStat

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        o_x_root = Xlib.display.Display().screen().root
        o_x_image = o_x_root.get_image(self.x, self.y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
        o_pil_image_rgb = PIL.Image.frombytes("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
        lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
        rgb = tuple(map(int, lf_colour))
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        self.print_info()
    
    def equals(self, r, g, b):
        if self.r == r and self.r == r and self.r == r:
            return True
        return False
    
    def print_info(self):
        print("Pixel:")
        print(self.r, self.g, self.b)