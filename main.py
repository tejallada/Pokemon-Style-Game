def main():
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






#runs the code
if __name__ == '__main__':
    main()
    