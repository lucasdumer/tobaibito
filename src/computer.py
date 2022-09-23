import wnck
import gtk
from config.environment import Environment
from window.window import Window
#from mouse import Mouse

class Computer:
    def __init__(self):
        self.environment = Environment()
        #self.mouse = Mouse()
        
    def get_windows(self):
        screen = Wnck.screen_get_default()
        while gtk.events_pending():
            gtk.main_iteration()
        screen_windows = screen.get_windows()
        windows = []
        for screen_window in screen_windows:
            if self.environment.get_window_name() in screen_window.get_name():
                window = Window(screen_window)
                window.map()
                windows.append(window)
        return windows
    
    #def get_mouse(self):
    #    return self.mouse