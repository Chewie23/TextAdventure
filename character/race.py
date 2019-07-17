#TODO
#Include special racial feats/traits

class GenericRace():
    def __init__(self):
        self.stat_changes = {}
        self.size = "Medium"
        self.type = "Humanoid"
        self.hp = 4

class Android(GenericRace):
    def __init__(self):
        self.stat_changes["DEX"] = 2
        self.stat_changes["INT"] = 2
        self.stat_changes["CHA"] = -2
        self.subtype = "Android"
        
class Human(GenericRace):
    def __init__(self):
        #+2 to any trait, so thus need to incorporate that
        self.subtype = "Human"
        
class Kasatha(GenericRace):
     def __init__(self):
        self.stat_changes["STR"] = 2
        self.stat_changes["WIS"] = 2
        self.stat_changes["INT"] = -2
        self.subtype = "Kasatha"
        
class Lashunta(GenericRace):
    def __init__(self):
        self.stat_changes["CHA"] = 2
        self.subtype = "Lashunta"
     
class KorashaLashunta(Lashunta):
    def __init__(self):
        self.stat_changes["STR"] = 2
        self.stat_changes["WIS"] = -2
        self.sub_subtype = "Korasha"

class DamayaLashunta(Lashunta):
    def __init__(self):
        self.stat_changes["INT"] = 2
        self.stat_changes["CON"] = -2
        self.sub_subtype = "Damaya"
        
class Shirrens(GenericRace):
    def __init__(self):
        self.stat_changes["CON"] = 2
        self.stat_changes["WIS"] = 2
        self.stat_changes["CHA"] = -2
        self.hp = 6
        self.subtype = "Shirren"
        
class Vesk(GenericRace):
    def __init__(self):
        self.stat_changes["STR"] = 2
        self.stat_changes["CON"] = 2
        self.stat_changes["INT"] = -2
        self.hp = 6
        self.subtype = "Vesk"
        

class Ysoki(GenericRace):
    def __init__(self):
        self.stat_changes["DEX"] = 2
        self.stat_changes["INT"] = 2
        self.stat_changes["STR"] = -2
        self.hp = 2
        self.size = "Small"
        self.subtype = "Ysoki"        
