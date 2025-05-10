
def print_instructions():
    print(f'You have alreqdy selected your pokemon.\n'
          f'''In this game your pokemon does not change any of your abilities.\n'''
          f'You will have to go through 5 levels to complete the game and then you can enter freeplay.\n\n'
          f'''When in a fight you have 5 options that vary in effectiveness based on your pokemon's level:\n'''
          f'1) Attack: you can attack your opponents pokemon\n'
          f'2) Block: You can attempt to block your opponents attack (will block a Super Attack 100% of the time)\n'
          f'3) Heal: You can heal your pokemon for a small amount of health\n'
          f'4) Charge: Gives you 1 more Super Charge\n'
          f'5) Super Attack: Attacks and wipes out your opponent (uses and requires 3 Charges)')



def main():

    freeplay_active = False


    # initial welcome message
    print('Welcome to the Pokemon Style Game!\n '
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
    print(yn_nick.lower())
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


#Introduction steps are complete now to move on to the actual game

    while not freeplay_active:
        print('\n\n\nGreetings traveler and welcome to the Pokemon-Style Game!\n'
              'This game is a simple version based off of the original pokemon games on the Nintendo DS\n'
              '_______________________________________________________\n')
        print_instructions()
        break







#runs the code
if __name__ == '__main__':
    main()
    