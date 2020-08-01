class Player():
    def __init__(self, name,):
        self.name = name
        self.choice = ""
        self.rounds_won = 0
        self.human_player = True

    def set_name(self, new_name):
        if len(new_name) ==0:
            pass
        else:
            self.name = new_name
