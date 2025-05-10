#This file contains the Pokemon class which is a class that gives the attributes of a pokemon

class Pokemon:

    #initializes the pokemon
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.level = 1
        fight_options = [attack, dodge, heal]

    #if the pokemon attacks
    def attack(self, other):

        #the other pokemon should have a random
        #chance that it gets hit here based on the level
#       of your pokemon and the level of that pokemon

