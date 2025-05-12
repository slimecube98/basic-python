import os

def add_vector(vector):
    x = float(input('Введите координату x: '))
    y = float(input('Введите координату y: '))
    vector.append((x, y))
    return vector

def vectors_menu():
    run = True

    vector1 = None
    vector2 = None

    while run:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Работа с векторами')
        print('1. Создать вектора')
        print('2. Вычислить длину вектора')
        print('3. Сложить два вектора')
        print('4. Вычесть два вектора')
        print('5. Умножить два вектора')
        print('6. Найти угол между двумя векторами')
        print('7. Проверить коллинеарность векторов')
        print('0. Вернуться в главное меню')

        choice = int(input('Выберите пункт меню: '))

        if choice == 1:
            
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 0:
            run = False
            print('Возврат в главное меню')

    pass
