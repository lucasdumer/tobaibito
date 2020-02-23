from map.dp_cn_map import DpCnMap
from window.screen_game_photo import ScreenGamePhoto

class World:
    def __init__(self):
        self.current_map = 0
        self.current_x = 0
        self.current_y = 0
        self.dp_cn_map = DpCnMap()

    def set_current_location_dp_cp_12_8(self, photo):
        self.current_map = 1
        self.current_x = 12
        self.current_y = 8
        self.dp_cn_map.sqms[8][12] = photo

    def photo_of_where_i_am(self, photo):
        for sqms in self.dp_cn_map.sqms:
            for sqm in sqms:
                if sqm == 0:
                    continue
                elif isinstance(sqm, ScreenGamePhoto):
                    print(sqm.equal(photo))
