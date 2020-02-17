import os

class Variable:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def get_value(self):
        return os.environ.get(self.name, "")
    
    def set_value(self, value):
        os.environ[self.name] = value