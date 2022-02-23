#Set_state classes

class keyboard_key:
    def __init__(self, letter, state = -1):
        self.letter = letter
        self.state = state

    def get_letter(self):
        return self.letter

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

#The boxes where you the text appears
class textBox:
    def __init__(self, letter, state = -1):
        self.letter = letter
        self.state = state

    def get_letter(self):
        return self.letter

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state