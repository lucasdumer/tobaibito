import wnck
import gtk
from config.environment import Environment
from window.window import Window

class Computer:
    def __init__(self):
        self.environment = Environment()
        
    def get_windows(self):
        screen = wnck.screen_get_default()
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
