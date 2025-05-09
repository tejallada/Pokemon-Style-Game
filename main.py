def main():
    print('Welcome to the Pokemon Style Game!\n '
          'Please type the name of your pokemon:\n'
          'Charmander, Squirtle, or Bulbasaur')
    my_pokemon = input('Pokemon: ')
    yn_nick = input(f'Do you want to name your {my_pokemon}? y/n ')
    nick = ''
    while True:
        if yn_nick.lower() == 'y':
            nick = input(f'What do you want to name your {my_pokemon}? ')
            break
        elif yn_nick.lower == 'n':
            nick = my_pokemon
            break
        else:
            print("Sorry that response is unable to be interpreted, please respond with 'y' or 'n'")
            yn_nick = input(f'Do you want to name your {my_pokemon}? y/n ')

if __name__ == main():
    main()
    