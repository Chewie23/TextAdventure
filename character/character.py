import generic_creature as gc

class Character(gc.Creature):
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    c = Character()
    c.name = "Lorc"
    print(c.name)
    c.check_stats()
