class ScreenGamePhoto:
    def __init__(
        self,
        sqm2x2,
        sqm3x3,
        sqm4x4,
        sqm4x6,
        sqm3x7,
        sqm2x8,
        sqm12x2,
        sqm11x3,
        sqm10x4,
        sqm10x6,
        sqm11x7,
        sqm12x8
    ):
        self.sqm2x2 = sqm2x2
        self.sqm3x3 = sqm3x3
        self.sqm4x4 = sqm4x4
        self.sqm4x6 = sqm4x6
        self.sqm3x7 = sqm3x7
        self.sqm2x8 = sqm2x8
        self.sqm12x2 = sqm12x2
        self.sqm11x3 = sqm11x3
        self.sqm10x4 = sqm10x4
        self.sqm10x6 = sqm10x6
        self.sqm11x7 = sqm11x7
        self.sqm12x8 = sqm12x8
    
    def equal(self, another_screen_game_photo):
        sqm_equal = 0
        if self.sqm2x2.equal(another_screen_game_photo.sqm2x2):
            sqm_equal = sqm_equal + 1

        if self.sqm3x3.equal(another_screen_game_photo.sqm3x3):
            sqm_equal = sqm_equal + 1

        if self.sqm4x4.equal(another_screen_game_photo.sqm4x4):
            sqm_equal = sqm_equal + 1

        if self.sqm4x6.equal(another_screen_game_photo.sqm4x6):
            sqm_equal = sqm_equal + 1

        if self.sqm3x7.equal(another_screen_game_photo.sqm3x7):
            sqm_equal = sqm_equal + 1

        if self.sqm2x8.equal(another_screen_game_photo.sqm2x8):
            sqm_equal = sqm_equal + 1

        if self.sqm12x2.equal(another_screen_game_photo.sqm12x2):
            sqm_equal = sqm_equal + 1

        if self.sqm11x3.equal(another_screen_game_photo.sqm11x3):
            sqm_equal = sqm_equal + 1

        if self.sqm10x4.equal(another_screen_game_photo.sqm10x4):
            sqm_equal = sqm_equal + 1

        if self.sqm10x6.equal(another_screen_game_photo.sqm10x6):
            sqm_equal = sqm_equal + 1

        if self.sqm11x7.equal(another_screen_game_photo.sqm11x7):
            sqm_equal = sqm_equal + 1

        if self.sqm12x8.equal(another_screen_game_photo.sqm12x8):
            sqm_equal = sqm_equal + 1
        
        return sqm_equal >= 9
