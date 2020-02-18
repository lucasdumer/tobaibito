import time
from pixel import Pixel
from config.environment import Environment
from mana import Mana

class Window:
    def __init__(self, screen):
        self.screen = screen
        self.environment = Environment()

    def focus(self):
        self.screen.activate(int(time.time()))

    def process_geometry(self):
        geometry = self.screen.get_geometry()
        self.screen_x = geometry[0]
        self.screen_y = geometry[1]
        self.width = geometry[2]
        self.height = geometry[3]

    def process_interface(self):
        i_didnt_find_everything_in_the_interface = True
        i_found_the_mana = False
        pixel_x = self.screen_x
        pixel_mana_y = self.environment.get_mana_pixel_shortcut()
        pixel_end_width = self.screen_x + self.width - 1
        while i_didnt_find_everything_in_the_interface:
            if i_found_the_mana == False:
                pixel = Pixel(pixel_x, pixel_mana_y)
                if pixel.its_a_pixel_of_mana():
                    i_found_the_mana = True
                    self.mana = Mana(pixel_x, pixel_mana_y)
                    pixel_mana_x = pixel_x + 1
                    for i in range(80):
                        pixel_mana = Pixel(pixel_mana_x + i, pixel_mana_y)
                        if pixel_mana.its_a_pixel_of_mana() == False:
                            i_found_the_mana = False
            if i_found_the_mana == True:
                i_didnt_find_everything_in_the_interface = False
            elif pixel_x == pixel_end_width and i_didnt_find_everything_in_the_interface:
                raise Exception("I didn't find everything in the interface!")
            else:
                pixel_x = pixel_x + 1

    def map(self):
        self.focus()
        self.process_geometry()
        self.process_interface()
        self.print_info()
    
    def observe(self):
        self.mana.observe()

    def print_info(self):
        print("Window:")
        print("screen_x -> ", self.screen_x)
        print("screen_y -> ", self.screen_y)
        print("width -> ", self.width)
        print("height -> ", self.height)

# import gtk
# import wnck
# # import pygame
# # from Xlib import display
# from config.environment import Environment
# import PIL.Image # python-imaging
# import PIL.ImageStat # python-imaging
# import Xlib.display # python-xlib
# from pynput.keyboard import Key, Controller

    # def focus(self):
    #     screen = wnck.screen_get_default()
    #     while gtk.events_pending():
    #         gtk.main_iteration()
    #     windows = screen.get_windows()
    #     for w in windows:
    #         if self.environment.get_window_name() in w.get_name():
    #             w.activate(int(time.time()))
                
    #     cicle = 0
    #     # pygame.init()
    #     # pygame.display.set_mode((1000, 1000))
    #     keyboard = Controller()
    #     while True:
    #         print("\nStart cicle!")
    #         print(cicle)

    #         # print self.get_pixel_colour(1000, 1000) azul escuro 60 60 61
    #         # print self.get_pixel_colour(900, 1000) vermelho 61 61 61
    #         # mouse_pos = pygame.mouse.get_pos()
    #         # print mouse_pos
    #         # 994 928
    #         # (39, 38, 38) vazio
    #         # rgb(0, 56, 116) cheio
    #         data = Xlib.display.Display().screen().root.query_pointer()._data
    #         print data["root_x"], data["root_y"]
    #         print self.get_pixel_colour(data["root_x"], data["root_y"])

    #         # y = 943
    #         y = 890
    #         # 359 943
    #         # 927 943
    #         # 568 = 100%
    #         # 5.68 = 1%
    #         start_live = self.get_pixel_colour(359, y)
    #         all_live = self.get_pixel_colour(927, y)

    #         if start_live[0] <> 0 or start_live[1] <> 175 or start_live[2] <> 0: # 100%
    #             if start_live[0] <> 184 or start_live[1] <> 140 or start_live[2] <> 8: # 50%
    #                 print "Cant see LIVE!!! -> ", start_live

    #         # need heal
    #         if all_live[0] == 37 and all_live[1] == 37 and all_live[2] == 36:
    #             print "f1"
    #             # keyboard.press(Key.f1)

    #             # live 50 exura vita
    #             # live 70 exura gran
    #             # live 85 exura

    #         # 1060 941
    #         all_mana = self.get_pixel_colour(1050, y)
    #         if all_mana[0] == 35 and all_mana[1] == 35 and all_mana[2] == 35:
    #             print "f3"
    #             keyboard.press(Key.f3)
    #             keyboard.release(Key.f3)
    #         else:
    #             print "all_mana", all_mana

    #         # start_live = self.get_pixel_colour(359, 943)
    #         # if start_live[0] <> 0 or start_live[1] <> 175 or start_live[2] <> 0:
    #         #     print "Cant see -> live_!"

    #         time.sleep(0.51)
    #         cicle += 1

    # def get_pixel_colour(self, i_x, i_y):
    #     o_x_root = Xlib.display.Display().screen().root
    #     o_x_image = o_x_root.get_image(i_x, i_y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
    #     o_pil_image_rgb = PIL.Image.frombytes("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
    #     lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
    #     return tuple(map(int, lf_colour))

    # def get_pixel_colour(self, i_x, i_y):
	#     o_gdk_pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
	#     o_gdk_pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), i_x, i_y, 0, 0, 1, 1)
    #     # return o_gdk_pixbuf.get_pixels_array().tolist()[0][0]
	#     return tuple(o_gdk_pixbuf.get_pixels_array().tolist()[0][0])

# python2.7 src/main.py