import time
from pokemon import Pokemon
import random

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
    my_pokemon_name = input('Pokemon: ').title()
    my_pokemon = Pokemon(my_pokemon_name)


    #checks if the user selected a listed Pokemon
    while True:
        if my_pokemon_name.title() == 'Charmander' or my_pokemon_name.title() == 'Squirtle' or my_pokemon_name.title() == 'Bulbasaur':
            break
        else:
            print("\nSorry that response is unable to be interpreted, please type one of the pokemon listed above.")
            my_pokemon_name = input('Pokemon: ').title()


    # user selects a nickname for their Pokemon
    yn_nick = input(f'\nDo you want to name your {my_pokemon_name}? y/n ')
    nick = ''
    while True:
        if yn_nick.lower() == 'y':
            nick = input(f'\nWhat do you want to name your {my_pokemon_name}? ')
            break
        elif yn_nick.lower() == 'n':
            nick = my_pokemon_name
            break
        else:
            print("\nSorry that response is unable to be interpreted, please respond with 'y' or 'n'")
            yn_nick = input(f'Do you want to name your {my_pokemon_name}? y/n ')
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
            #figures out what opponent you are fighting
            if game_level == 1:
                foe = 'James'
                foe_pokemon = Pokemon('Koffing', 2)
            elif game_level == 2:
                foe = 'Jessie'
                foe_pokemon = Pokemon('Ekans', 4)
            elif game_level == 3:
                foe = 'Meowth'
                foe_pokemon = Pokemon('Meowth', 5)
            elif game_level == 4:
                foe = 'Wobbuffet'
                foe_pokemon = Pokemon('Wobbuffet', 8)
            elif game_level == 5:
                foe = 'Brock'
                foe_pokemon = Pokemon('Onyx', 13)
            else:
                freeplay_foe_list = ['Misty', 'Nurse Joy', 'Officer Jenny', 'Proffessor Oak']
                freeplay_pokemon_list = ['Gyarados', 'Sandslash', 'Lapras', 'Machamp', 'Golbat', 'Snorlax', 'Primeape']
                foe = freeplay_foe_list[random.randint(4)-1]
                foe_pokemon = Pokemon(freeplay_foe_list[random.randint(7) - 1], 8)
        
        def print_battle_menu():
            print(  f'1) Attack: you can attack your opponents pokemon\n'
                    f'2) Block: You can attempt to block your opponents attack (will block a Super Attack 100% of the time)\n'
                    f'3) Heal: You can heal your pokemon for a small amount of health\n'
                    f'4) Charge: Gives you 1 more Super Charge\n'
                    f'5) Super Attack: Attacks and wipes out your opponent (uses and requires 3 Charges)')
            local_battle_selection = input('What would you like to do? ')
            return local_battle_selection
            
            
                
            #actual battle scenario
            print(f"You are now battling {foe}'s {foe_pokemon}!")

            while battle:
                my_pokemon.block_status = False
                battle_selection = print_battle_menu()

                if battle_selection == 1:
                    my_pokemon.attack(foe_pokemon)
                elif battle_selection == 2:
                    my_pokemon.block_status == True

















            #runs the code
if __name__ == '__main__':
    main()
    