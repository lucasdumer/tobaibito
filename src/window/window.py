import time
from pixel import Pixel
from config.environment import Environment
from mana import Mana
from life import Life
from keyboard import Keyboard
from battle_list import Battle_list

class Window:
    def __init__(self, screen):
        self.screen = screen
        self.environment = Environment()
        self.keyboard = Keyboard()

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
        i_found_the_life = False
        i_found_the_mana = False
        pixel_x = self.screen_x
        pixel_life_y = self.environment.get_mana_and_life_pixel_shortcut()
        pixel_mana_y = self.environment.get_mana_and_life_pixel_shortcut()
        pixel_end_width = self.screen_x + self.width - 1
        while i_didnt_find_everything_in_the_interface:

            if i_found_the_life == False:
                pixel = Pixel(pixel_x, pixel_life_y)
                if pixel.its_a_pixel_of_life():
                    i_found_the_life = True
                    self.life = Life(pixel_x, pixel_life_y)
                    pixel_life_x = pixel_x + 1
                    for i in range(80):
                        pixel_live = Pixel(pixel_life_x + i, pixel_life_y)
                        if pixel_live.its_a_pixel_of_life() == False:
                            i_found_the_life = False

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

            if i_found_the_mana == True and i_found_the_life == True:
                i_didnt_find_everything_in_the_interface = False
            elif pixel_x == pixel_end_width and i_didnt_find_everything_in_the_interface:
                print(i_found_the_life, i_found_the_mana)
                raise Exception("I didn't find everything in the interface!")
            else:
                pixel_x = pixel_x + 1
        
        self.battle_list = Battle_list(989, 97)

    def map(self):
        self.focus()
        self.process_geometry()
        self.process_interface()
        self.print_info()
        self.keyboard.execute_bot_confirmation_command()
    
    def observe(self):
        self.life.observe()
        self.mana.observe()
        self.battle_list.observe()

    def print_info(self):
        print("Window:")
        print("screen_x -> ", self.screen_x)
        print("screen_y -> ", self.screen_y)
        print("width -> ", self.width)
        print("height -> ", self.height)
