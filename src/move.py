from keyboard import Keyboard

class Move:
    def __init__(self):
        self.keyboard = Keyboard()

    def top(self):
        self.keyboard.up()
    
    def right(self):
        self.keyboard.right()
    
    def down(self):
        self.keyboard.down()
    
    def left(self):
        self.keyboard.left()

    