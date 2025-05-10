import time
from pokemon import Pokemon

#game progress
game_level = 1








#prints the instructions for the user
def print_instructions():
    print(f'You have already selected your pokemon.\n'
          f'''In this game your pokemon does not change any of your abilities.\n'''
          f'You will have to go through 5 levels to complete the game and then you can enter freeplay.\n\n'
          f'''When in a fight you have 5 options that vary in effectiveness based on your pokemon's level:\n'''
          f'1) Attack: you can attack your opponents pokemon\n'
          f'2) Block: You can attempt to block your opponents attack (will block a Super Attack 100% of the time)\n'
          f'3) Heal: You can heal your pokemon for a small amount of health\n'
          f'4) Charge: Gives you 1 more Super Charge\n'
          f'5) Super Attack: Attacks and wipes out your opponent (uses and requires 3 Charges)')

#prints the option menu for the player to choose
def print_menu():
    print('Please select one of the options:\n'
          '1) View your pokemons stats\n'
          '2) Battle\n'
          '3) Exit the program\n')
    output = input('Type your selection here: ')
    return output


def main():

    freeplay_active = False


    # initial welcome message
    print('Welcome to the Pokemon Style Game!\n'
          'Please type the name of your pokemon:\n'
          'Charmander, Squirtle, or Bulbasaur')
    my_pokemon = input('Pokemon: ').title()


    #checks if the user selected a listed Pokemon
    while True:
        if my_pokemon.title() == 'Charmander' or my_pokemon.title() == 'Squirtle' or my_pokemon.title() == 'Bulbasaur':
            break
        else:
            print("\nSorry that response is unable to be interpreted, please type one of the pokemon listed above.")
            my_pokemon = input('Pokemon: ').title()


    # user selects a nickname for their Pokemon
    yn_nick = input(f'\nDo you want to name your {my_pokemon}? y/n ')
    nick = ''
    while True:
        if yn_nick.lower() == 'y':
            nick = input(f'\nWhat do you want to name your {my_pokemon}? ')
            break
        elif yn_nick.lower() == 'n':
            nick = my_pokemon
            break
        else:
            print("\nSorry that response is unable to be interpreted, please respond with 'y' or 'n'")
            yn_nick = input(f'Do you want to name your {my_pokemon}? y/n ')
        time.sleep(1)


#Introduction steps are complete now to move on to the actual game

    while not freeplay_active:
        battle = False

        print('\n\n\nGreetings traveler and welcome to the Pokemon-Style Game!\n'
              'This game is a simple version based off of the original pokemon games on the Nintendo DS\n'
              '_______________________________________________________\n')
        time.sleep(2)
        print_instructions()
        time.sleep(5)
        print('')
        menu_option = print_menu()
        print(menu_option)

        if menu_option == 1:
        #print the stats of the pokemon using the print_stats method in pokemon.py
            print('placeholder for stats\n'
                  'blah\n'
                  'blah\n'
                  'blah')
        elif menu_option == 2:
            battle = True
            #this is the battle option
        elif menu_option == 3:
            break
        else:
            print('\n\n\n')


        if battle:

            if game_level == 1:
                foe = 'James'
                foe_pokemon = Pokemon('Squirtle', 2)
            if game_level == 2:
                foe = 'Jessie'
                foe_pokemon = Pokemon('Charmander', 4)












            #runs the code
if __name__ == '__main__':
    main()
    