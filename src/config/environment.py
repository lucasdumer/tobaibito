from config.variable import Variable

class Environment:
    def __init__(self):
        self.variables = {
            'toba_bot_off': None,
            'toba_bot_on_heal_life_mana': None,
            'toba_bot_on_heal_mana_utamo': None,
            'toba_bot_on_heal_mana': None,
            'TOBAIBITO_WINDOW_NAME': None,
            'TOBAIBITO_LIFE_DARK_R': 179,
            'TOBAIBITO_LIFE_DARK_G': 133,
            'TOBAIBITO_LIFE_DARK_B': 133,
            'TOBAIBITO_LIFE_RED_R': 225,
            'TOBAIBITO_LIFE_RED_G': 133,
            'TOBAIBITO_LIFE_RED_B': 133,
            'TOBAIBITO_LIFE_RED2_R': 225,
            'TOBAIBITO_LIFE_RED2_G': 156,
            'TOBAIBITO_LIFE_RED2_B': 156,
            'TOBAIBITO_LIFE_YELLOW_R': 230,
            'TOBAIBITO_LIFE_YELLOW_G': 207,
            'TOBAIBITO_LIFE_YELLOW_B': 137,
            'TOBAIBITO_LIFE_OK_R': 186,
            'TOBAIBITO_LIFE_OK_G': 210,
            'TOBAIBITO_LIFE_OK_B': 135,
            'TOBAIBITO_LIFE_FULL_R': 133,
            'TOBAIBITO_LIFE_FULL_G': 225,
            'TOBAIBITO_LIFE_FULL_B': 133,
            'TOBAIBITO_MANA_R': 0,
            'TOBAIBITO_MANA_G': 93,
            'TOBAIBITO_MANA_B': 194,
            'TOBAIBITO_MANA_AND_LIFE_PIXEL_SHORTCUT': 70,
            'TOBAIBITO_AUTO_POTION_MANA': 90,
            'TOBAIBITO_AUTO_HEAL_LOW': 90,
            'TOBAIBITO_AUTO_HEAL_MEDIUM': 75,
            'TOBAIBITO_AUTO_HEAL_STRONG': 50
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
        # self.check_for_required_variable(variable)
        self.variables[variable].set_value(value)
    
    def get(self, variable):
        # self.check_for_required_variable(variable)
        return self.variables[variable].get_value()
    
    def get_window_name(self):
        return self.get('TOBAIBITO_WINDOW_NAME')

    def get_life_r(self):
        return int(self.get('TOBAIBITO_LIFE_R'))
    
    def get_life_g(self):
        return int(self.get('TOBAIBITO_LIFE_G'))

    def get_life_b(self):
        return int(self.get('TOBAIBITO_LIFE_B'))

    def get_mana_r(self):
        return int(self.get('TOBAIBITO_MANA_R'))
    
    def get_mana_g(self):
        return int(self.get('TOBAIBITO_MANA_G'))

    def get_mana_b(self):
        return int(self.get('TOBAIBITO_MANA_B'))

    def get_mana_and_life_pixel_shortcut(self):
        return int(self.get('TOBAIBITO_MANA_AND_LIFE_PIXEL_SHORTCUT'))

    def get_auto_potion_mana(self):
        return int(self.get('TOBAIBITO_AUTO_POTION_MANA'))

    def get_auto_heal_low(self):
        return int(self.get('TOBAIBITO_AUTO_HEAL_LOW'))

    def get_auto_heal_medium(self):
        return int(self.get('TOBAIBITO_AUTO_HEAL_MEDIUM'))

    def get_auto_heal_strong(self):
        return int(self.get('TOBAIBITO_AUTO_HEAL_STRONG'))

    def show(self):
        s = ""
        last_key = list(self.variables.keys())[-1]
        for key, value in self.variables.items():
            s += key + " -> " + value.get_value()
            if key != last_key:
                s += "\n"
        print(s)