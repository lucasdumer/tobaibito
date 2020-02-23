from sqm import Sqm
from screen_game_photo import ScreenGamePhoto

class ScreenGame:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sqm_w = self.w / 15
        self.sqm_h = self.h / 11

    # 15, 11
    # 14, 10
    def get_sqm(self, x, y):
        sqm_x = self.x + (self.sqm_w * x)
        sqm_y = self.y + (self.sqm_h * y)
        return Sqm(sqm_x, sqm_y, self.sqm_w, self.sqm_h)

    def take_photo(self):
        return ScreenGamePhoto(
            self.get_sqm(2, 2),
            self.get_sqm(3, 3),
            self.get_sqm(4, 4),
            self.get_sqm(4, 6),
            self.get_sqm(3, 7),
            self.get_sqm(2, 8),
            self.get_sqm(12, 2),
            self.get_sqm(11, 3),
            self.get_sqm(10, 4),
            self.get_sqm(10, 6),
            self.get_sqm(11, 7),
            self.get_sqm(12, 8)
        )