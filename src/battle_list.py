import time
from pixel import Pixel
from keyboard import Keyboard
from move import Move

class Battle_list:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.keyboard = Keyboard()
        self.last_move_time = time.time()
        self.sqm = -10
        self.move  = Move()

    def observe(self):
        pixel = Pixel(self.x, self.y)
        pixel2 = Pixel(966, 98)

        if pixel.its_a_pixel_of_live_in_battle_list() and pixel2.its_a_pixel_atk_target() == False:
            self.keyboard.space()
        # elif pixel2.its_a_pixel_atk_target() == False:
        #     now = time.time()
        #     elapsed = now - self.last_move_time
        #     if (elapsed > 2):
        #         print(elapsed)

        #         if -10 <= self.sqm <= 32:
        #             self.move.right()
        #         elif 33 <= self.sqm <= 35:
        #             self.move.down()
        #         elif 36 <= self.sqm <= 37:
        #             self.move.right()
        #         elif 38 <= self.sqm <= 38:
        #             self.move.down()
        #         elif 39 <= self.sqm <= 48:
        #             self.move.right()
        #         elif 48 <= self.sqm <= 58:
        #             self.move.left()
        #         elif 59 <= self.sqm <= 59:
        #             self.move.top()
        #         elif 60 <= self.sqm <= 62:
        #             self.move.left()
        #         elif 63 <= self.sqm <= 65:
        #             self.move.top()
        #         elif 66 <= self.sqm <= 120:
        #             self.move.left()

# r7
# d3
# 10l
# 6d
                # if 1 <= self.sqm <= 6:
                #     self.move.right()
                # elif 7 <= self.sqm <= 9:
                #     self.move.down()
                # elif 10 <= self.sqm <= 19:
                #     self.move.left()
                # elif 20 <= self.sqm <= 25:
                #     self.move.down()
# 10l
# 7d
# 1l
# 9d
                # elif 26 <= self.sqm <= 35:
                #     self.move.left()
                # elif 36 <= self.sqm <= 42:
                #     self.move.down()
                # elif 43 <= self.sqm <= 43:
                #     self.move.left()
                # elif 44 <= self.sqm <= 52:
                #     self.move.down()
# 14l
# 14u
# 11d
# 14r
                # elif 53 <= self.sqm <= 66:
                #     self.move.left()
                # elif 67 <= self.sqm <= 80:
                #     self.move.top()
                # elif 81 <= self.sqm <= 91:
                #     self.move.down()
                # elif 92 <= self.sqm <= 105:
                #     self.move.right()

# 12u
# 9r
# 5u
# 4r
                # elif 106 <= self.sqm <= 117:
                #     self.move.top()
                # elif 118 <= self.sqm <= 126:
                #     self.move.right()
                # elif 127 <= self.sqm <= 131:
                #     self.move.top()
                # elif 132 <= self.sqm <= 135:
                #     self.move.right()

# 5u
# 1r
                # elif 136 <= self.sqm <= 140:
                #     self.move.top()
                # elif 141 <= self.sqm <= 141:
                #     self.move.right()
                # else:
                #     self.sqm = -10

                # self.last_move_time = time.time()
                # # print(self.sqm)
                # self.sqm = self.sqm + 1