#TODO
#Have this guy be the master and commander of all data
#Themes, race, name, stat blocks, etc

import sys
#sys.path.insert(0, <SOME RELATIVE PATH HERE>)

import statblock

#This is will be the long lived class that will hold all the information
class Character():
    def __init__(self):
        self._name = ""
        self.theme = ""
        self._class = ""
        self.skills
        self.sb = statblock.StatBlock()
   
    #Properties are weird but useful. Need to use a semi-private variable of 
    #"_name" to not create a recursive loop that never ends
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def check_stats(self):
        for k, v in self.sb.stats_block.items():
            print("{} stat: {}".format(k, v))
        
    def check_ability_mod(self):
        for k, v in self.stat_block.ability_mod_block.items():
            print("{} modifier: {}".format(k, v))

if __name__ == "__main__":
    c = Character()
    c.name = "Lorc"
    print(c.name)
    c.check_stats()
