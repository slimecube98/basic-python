import os
from individual.MyMath.Vector import Vector
from individual.Menu.vector_menu import vectors_menu


def main():
    run = True

    while run:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Главное меню')
        print('1. Работа с векторами')

        print('0. Выход')
        choice = int(input('Выберите пункт меню: '))

        if choice == 1:
            vectors_menu()
        
        if choice == 0:
            run = False
            print('Выход из программы')

    
    pass


if __name__ == "__main__":
    main()