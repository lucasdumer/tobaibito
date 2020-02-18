import Xlib.display

class Mouse:
    def get_x(self):
        data = Xlib.display.Display().screen().root.query_pointer()._data
        return data["root_x"]

    def get_y(self):
        data = Xlib.display.Display().screen().root.query_pointer()._data
        return data["root_y"]
    
    def print_info(self):
        print("Mouse:")
        print("X -> ", self.get_x())
        print("Y -> ", self.get_y())