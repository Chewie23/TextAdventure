#Not sure how abstract or how centralized this should be?
#One one hand, nice to have everything in a big class
#On the other, it's probably better sanity for modularizing
class Creature():
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
        self.feat_dict = {}
        self.inventory = {}
        self.bulk = 0


    def calculate_ability_mod(self):
        ability_mod_block = {"str": 0, "dex": 0, "con": 0,
                                  "int": 0, "wis": 0, "cha": 0}
        for e in range(6):
            ability_mod_block[self.stat_keys[e]] = (self.stats_block[e] - 10) / 2
        return ability_mod_block

    def calculate_bulk_limits(self):
        if self.bulk <= (self.str / 2):
            self.bulk_limit = "Normal"
        elif self.bulk > (self.str / 2):
            self.bulk_limit = "Encumbered"
        elif self.bulk >= self.str:
            self.bulk_limit = "Overburdened"
        
    def calculate_bulk(self):
        bulk_sum = 0
        for bulk in self.inventory.values():
            bulk_sum += bulk
        self.bulk = bulk_sum


    def check_stats(self):
        for e in range(6):
            print("{}: {}".format(self.stat_keys[e], self.stats_block[e]))

    def get_ability_mod(self):
        return self.ability_mod_block




if __name__ == "__main__":
    c = Creature(10, 12, 13, 12, 14, 3)
    print(c.get_ability_mod())
    c.check_stats()
