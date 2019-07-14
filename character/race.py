#TODO
#Organize the structure of data
#   Do I want one abstract class that all SF_classes rely on?
#   Have each SF_class hold its own data, like below?
#   Have on monolithic class that contains ALL SF_classes?

class Android():
    def __init__(self):
        self.stat_changes["DEX"] = 2
        self.stat_changes["INT"] = 2
        self.stat_changes["CHA"] = -2
        self.hp = 4
