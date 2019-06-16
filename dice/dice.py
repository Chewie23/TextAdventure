import random
import time

class Dice():
    def __init__(self):
        self.dice_bag = [4, 6, 8, 10, 12, 20, 100]

    def roll_dice(self, dice_string):
        #Assumes the string will be in the format of "1d4" or "4d6"
        sum_of_roll = 0
        dice_num = int(dice_string[0])
        dice_type = int(dice_string[2])

        random.seed(time.time())
        for n in range(dice_num):
            sum_of_roll += random.randrange(1, dice_type + 1)
        return sum_of_roll

if __name__ == "__main__":
    d = Dice()
    print(d.roll_dice("2d4"))
