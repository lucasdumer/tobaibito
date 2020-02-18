from config.variable import Variable

class Environment:
    def __init__(self):
        self.variables = {
            'TOBAIBITO_WINDOW_NAME': None,
            'TOBAIBITO_MANA_R': 0,
            'TOBAIBITO_MANA_G': 93,
            'TOBAIBITO_MANA_B': 194,
            'TOBAIBITO_MANA_PIXEL_SHORTCUT': 931
        }
        for i in self.variables.keys():
            self.variables[i] = Variable(i)
    
    def check_for_variable(self, variable):
        return variable in self.variables

    def check_for_required_variable(self, variable):
        if not self.check_for_variable(variable):
            raise Exception("environment variable '" + variable + "' is not valid")

    def variable_must_have_value(self, variable):
        self.check_for_required_variable(variable)
        if self.variables[variable] is None or self.variables[variable] == '':
            raise Exception("environment variable '" + variable + "' is required")

    def check_required_environment_variables_filled_in(self):
        self.variable_must_have_value('MCW_GIT_REMOTE')

    def set(self, variable, value):
        self.check_for_required_variable(variable)
        self.variables[variable].set_value(value)
    
    def get(self, variable):
        self.check_for_required_variable(variable)
        return self.variables[variable].get_value()
    
    def get_window_name(self):
        return self.get('TOBAIBITO_WINDOW_NAME')

    def get_mana_r(self):
        return int(self.get('TOBAIBITO_MANA_R'))
    
    def get_mana_g(self):
        return int(self.get('TOBAIBITO_MANA_G'))

    def get_mana_b(self):
        return int(self.get('TOBAIBITO_MANA_B'))

    def get_mana_pixel_shortcut(self):
        return int(self.get('TOBAIBITO_MANA_PIXEL_SHORTCUT'))

    def show(self):
        s = ""
        last_key = list(self.variables.keys())[-1]
        for key, value in self.variables.items():
            s += key + " -> " + value.get_value()
            if key != last_key:
                s += "\n"
        print(s)