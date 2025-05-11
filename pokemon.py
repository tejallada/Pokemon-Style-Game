#This file contains the Pokemon class which is a class that gives the attributes of a pokemon
import random
class Pokemon:

    #initializes the pokemon
    def __init__(self, name, level = 1):
        self.name = name
        self.level = level
        self.health = 100 + (50 * level)
        self.experience = 0
        self.block_status = False
        self.charge_count = 0

    #if the pokemon has enough xp then the pokemon should level up
    def level_up(self):
        while self.experience >= 100:
            self.level += 1
            self.experience = self.experience - 100
            print('------\n'
                  f'{self.name} has leveled up!'
                  '------\n')

    #if the pokemon attacks
    def attack(self, other):
        if not self.block_status:
            other.health -= random.randint(10, 75) * self.level

    def heal(self):
        heal_amount = random.randint(3) * 10 * self.level//2
        self.health += heal_amount

