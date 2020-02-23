from __future__ import division
from pixel import Pixel

class Sqm:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        w1 = self.w / 100
        h1 = self.h / 100
        
        pixel30x = (self.x + (w1 * 30))
        pixel60x = (self.x + (w1 * 60))
        pixel90x = (self.x + (w1 * 90))

        pixel30y = (self.y + (h1 * 30))
        pixel60y = (self.y + (h1 * 60))
        pixel90y = (self.y + (h1 * 90))

        self.pixel30x30 = Pixel(pixel30x, pixel30y)
        self.pixel30x60 = Pixel(pixel30x, pixel60y)
        self.pixel30x90 = Pixel(pixel30x, pixel90y)
        self.pixel60x30 = Pixel(pixel60x, pixel30y)
        self.pixel60x60 = Pixel(pixel60x, pixel60y)
        self.pixel60x90 = Pixel(pixel60x, pixel90y)
        self.pixel90x30 = Pixel(pixel90x, pixel30y)
        self.pixel90x60 = Pixel(pixel90x, pixel60y)
        self.pixel90x90 = Pixel(pixel90x, pixel90y)
    
    def equal(self, another_sqm):
        pixel_equal = 0
        if self.pixel30x30.equal(another_sqm.pixel30x30):
            pixel_equal = pixel_equal + 1

        if self.pixel30x60.equal(another_sqm.pixel30x60):
            pixel_equal = pixel_equal + 1

        if self.pixel30x90.equal(another_sqm.pixel30x90):
            pixel_equal = pixel_equal + 1

        if self.pixel60x30.equal(another_sqm.pixel60x30):
            pixel_equal = pixel_equal + 1

        if self.pixel60x60.equal(another_sqm.pixel60x60):
            pixel_equal = pixel_equal + 1

        if self.pixel60x90.equal(another_sqm.pixel60x90):
            pixel_equal = pixel_equal + 1

        if self.pixel90x30.equal(another_sqm.pixel90x30):
            pixel_equal = pixel_equal + 1

        if self.pixel90x60.equal(another_sqm.pixel90x60):
            pixel_equal = pixel_equal + 1

        if self.pixel90x90.equal(another_sqm.pixel90x90):
            pixel_equal = pixel_equal + 1
        
        return pixel_equal >= 8