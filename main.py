import time
from pokemon import Pokemon
import random

#game progress
game_level = 1

#prints the battle menu for the user
def print_battle_menu():
    print(f'1) Attack: you can attack your opponents pokemon\n'
          f'2) Block: You can attempt to block your opponents attack (will block a Super Attack 100% of the time)\n'
          f'3) Heal: You can heal your pokemon for a small amount of health\n'
          f'4) Charge: Gives you 1 more Super Charge\n'
          f'5) Super Attack: Attacks and wipes out your opponent (uses and requires 3 Charges)')
    local_battle_selection = int(input('What would you like to do? '))
    return local_battle_selection


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
    return int(output)


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
    print('\n\n\nGreetings traveler and welcome to the Pokemon-Style Game!\n'
          'This game is a simple version based off of the original pokemon games on the Nintendo DS\n'
          '_______________________________________________________\n')
    time.sleep(2)

    while not freeplay_active:
        battle = False


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

        foe = ''
        foe_pokemon = ''
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
                foe = freeplay_foe_list[random.randint(1,4)-1]
                foe_pokemon = Pokemon(freeplay_foe_list[random.randint(1,7) - 1], 8)
            
            
                
            #actual battle scenario
            print(f"\nYou are now battling {foe}'s {foe_pokemon.name}!\n")

            while battle:
                foe_move_selection = 1
                my_pokemon.block_status = False
                battle_selection = print_battle_menu()
                if foe_pokemon.charge_count >= 3:
                    if random.randint(1, 5) >= 2:
                        foe_move_selection = 5
                    else:
                        foe_move_selection = random.randint(1,4)
                else:
                    foe_move_selection = random.randint(1,4)


                #your battle selection
                if battle_selection == 1:
                    my_pokemon.attack(foe_pokemon)
                    print(f'{nick} attacked {foe_pokemon.name}!')
                    print(f'{foe_pokemon.name} has only {foe_pokemon.health} remaining.')
                elif battle_selection == 2:
                    my_pokemon.block_status == True
                elif battle_selection == 3:
                    my_pokemon.heal()
                elif battle_selection == 4:
                    my_pokemon.charge_count += 1
                elif battle_selection == 5:
                    if my_pokemon.charge_count >= 3:
                        if foe_move_selection != 2:
                            foe_pokemon.health = 0
                        else:
                            print(f"{foe}'s {foe_pokemon.name} had a block ready!")
                time.sleep(5)


                #foe's battle selection
                if foe_move_selection == 1:
                    foe_pokemon.attack(my_pokemon)
                    print(f'{foe_pokemon.name} ATTACKED {nick}!')
                    print(f'{nick} now has only {my_pokemon.health} HP remaining.')
                elif foe_move_selection == 3:
                    foe_pokemon.heal()
                    print(f'{foe_pokemon.name} HEALED themselves!')
                    print(f'{foe_pokemon.name} now has {foe_pokemon.health} HP remaining')
                elif foe_move_selection == 4:
                    foe_pokemon.charge_count += 1
                    print(f'{foe_pokemon.name} has CHARGED themselves!')
                    print(f"{foe_pokemon.name} now has {foe_pokemon.charge_count}'s remaining")
                elif foe_move_selection == 5:
                    if foe_pokemon.charge_count >= 3:
                        print(f'{foe_pokemon.name} attacked {nick} with a SUPER ATTACK!')
                        if battle_selection == 2:
                            my_pokemon.health = 0
                            print(f'Critical Hit! {nick} has fainted!')
                            battle = False
                        else:
                            print(f"{my_pokemon.name} had a BLOCK ready!")























            #runs the code
if __name__ == '__main__':
    main()
    