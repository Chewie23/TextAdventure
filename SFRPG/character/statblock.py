#Chose to have relative because it'll be universal, instead of doing some 
#weird absolute path that is compatible with Cygwin and MacOS
import collections as c
import sys
sys.path.insert(0, '../dice')

import dice as d

class StatBlock():
    def __init__(self):
        self.stats_block = c.OrderedDict([("STR", 0), ("DEX", 0), ("CON", 0),
                            ("INT", 0), ("WIS", 0), ("CHA", 0) ] )

        self.roll_stats()
        self.ability_mod_block = self.calculate_ability_mod()


    def calculate_ability_mod(self):
        ability_mod_block = c.OrderedDict([("STR", 0), ("DEX", 0), ("CON", 0),
                            ("INT", 0), ("WIS", 0), ("CHA", 0) ] )
        for key, val in self.stats_block.items():
            ability_mod_block[key] = (val - 10) // 2
        return ability_mod_block
        
    def roll_stats(self):
        dice = d.Dice()
        for key in self.stats_block.keys():
            roll = dice.roll_dice("4d6")
            roll.remove( min(roll) )
            
            stat_sum = sum( roll )
            self.stats_block[key] = stat_sum
            
if __name__ == "__main__":
    s = StatBlock()
    s.roll_stats()
    print(s.stats_block)
