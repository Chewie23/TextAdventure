#TODO
#Auto-generate random stats
#Can "re-roll" as many times as the player likes

class StatBlock():
    def __init__(self, STR = 0 , DEX = 0, CON = 0, INT = 0, WIS = 0, CHA = 0):
        self.stat_keys = ["str", "dex", "con", "int", "wis", "cha"]

        self.str = STR
        self.dex = DEX
        self.con = CON
        self.int = INT
        self.wis = WIS
        self.cha = CHA

        self.stats_block = [self.str, self.dex, self.con,
                            self.int, self.wis, self.cha]

        self.ability_mod_block = self.calculate_ability_mod()


    def calculate_ability_mod(self):
        ability_mod_block = {"str": 0, "dex": 0, "con": 0,
                                  "int": 0, "wis": 0, "cha": 0}
        for e in range(6):
            ability_mod_block[self.stat_keys[e]] = (self.stats_block[e] - 10) / 2
        return ability_mod_block