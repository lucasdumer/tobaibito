from map.dp_cn_map import DpCnMap
from window.screen_game_photo import ScreenGamePhoto

class World:
    def __init__(self):
        self.current_map = 0
        self.current_x = 0
        self.current_y = 0
        self.dp_cn_map = DpCnMap()

    def set_map_x_y(self, map, x, y):
        self.current_map = map
        self.current_x = x
        self.current_y = y

    def get_current_map(self):
        if self.current_map == 1:
            return self.dp_cn_map

    def photo_of_where_i_am(self, photo):
        x = -1
        y = -1
        for sqms in self.get_current_map().sqms:
            y = y + 1
            for sqm in sqms:
                x = x + 1
                if isinstance(sqm, ScreenGamePhoto):
                    if sqm.equal(photo):
                        self.current_x = x
                        self.current_y = y
                        print("true")
            x = -1
        print(self.current_x, self.current_y)
