import os
# from MyMath.Vector import Vector
from MyMath.Vector import Vector

def create_vector():
    x = int(input('Введите координату x: '))
    y = int(input('Введите координату y: '))
    return Vector(coordinates = [x, y])


def vectors_menu():
        run = True

        vector1 = None
        vector2 = None

        while run:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Работа с векторами')
                print('1. Создать вектора')

                if vector1 is not None and vector2 is not None:
                    print('2. Сложить два вектора')
                    print('3. Вычесть два вектора')
                    print('4. Умножить два вектора')
                    print('5. Найти угол между двумя векторами')
                    print('6. Проверить коллинеарность векторов')

                print('0. Вернуться в главное меню')

                choice = int(input('Выберите пункт меню: '))

                # Проверка на создание векторов
                # Если векторы не созданы, то можно только создать их
                if vector1 is None and vector2 is None and choice not in [1, 0]:
                    print('Векторы не созданы, создайте их')
                    input('Нажмите Enter, чтобы продолжить...')
                    continue

                if choice == 1:
                    print('Создание ветора 1:')
                    vector1 = create_vector()

                    if vector1 is None:
                        print('Ошибка при создании вектора 1')
                        input('Нажмите Enter, чтобы продолжить...')
                        continue


                    print('Создание ветора 2:')
                    vector2 = create_vector()
                    if vector2 is None:
                        print('Ошибка при создании вектора 2')
                        input('Нажмите Enter, чтобы продолжить...')
                        continue

                    print('Векторы созданы')
                    pass
                elif choice == 2:
                    print('Сложение векторов:', vector1, ' + ', vector2)
                    print('Результат:', vector1 + vector2)
                elif choice == 3:
                    print('Вычитание векторов:', vector1, ' - ' , vector2)
                    print('Результат:', vector1 - vector2)
                elif choice == 4:
                    print('Умножение векторов:', vector1, ' * ', vector2)
                    print('Результат:', vector1 * vector2)
                elif choice == 5:
                    print('Угол между векторами:', vector1, ' и ', vector2)
                    print('Результат:', vector1.angle_between(vector2))
                elif choice == 6:
                    print('Проверка коллинеарности векторов:', vector1, ' и ', vector2)
                    print('Результат:', vector1.is_collinear_with(vector2))
                elif choice == 0:
                    run = False
                    if vector1 is not None: del vector1
                    if vector2 is not None: del vector2
                    print('Возврат в главное меню')
                else:
                    print('Некорректный ввод, попробуйте еще раз')
                    
                input('Нажмите Enter, чтобы продолжить...')
            except Exception as e:
                print('Ошибка:', e)
                input('Нажмите Enter, чтобы продолжить...')