import os
# from MyMath.Vector import Vector
from MyMath.Matrix import Matrix
from Menu.vector_menu import create_vector

def create_matrix():
    rows = []
    rows_count = int(input('Введите количество строк: '))
    cols_count = int(input('Введите количество столбцов: '))
    for i in range(rows_count):
        val = input('Введите элементы строки через пробел: ')
        row = [int(x) for x in val.split()]
        if len(row) != cols_count:
            print('Количество элементов в строке не совпадает с количеством столбцов')
            return None
        rows.append(row)
    return Matrix(rows)


def matrices_menu():
        run = True

        matrix1 = None
        matrix2 = None

        while run:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Работа с матрицами')
                print('1. Создать матрицы')

                if matrix1 is not None and matrix2 is not None:
                    print('2. Сложить две матрицы')
                    print('3. Вычесть две матрицы')
                    print('4. Умножить матрицу на вектор')
                    print('5. Умножить матрицу на матрицу')
                    print('6. Транспонировать матрицы')
                    print('7. Определители матриц')
                    print('8. Решение СЛАУ методом Гаусса')

                print('0. Вернуться в главное меню')

                choice = int(input('Выберите пункт меню: '))

                # Проверка на создание векторов
                # Если векторы не созданы, то можно только создать их
                if matrix1 is None and matrix2 is None and choice not in [1, 0]:
                    print('Векторы не созданы, создайте их')
                    input('Нажмите Enter, чтобы продолжить...')
                    continue

                if choice == 1:
                    print('Создание матрицы 1:')
                    matrix1 = create_matrix()
                    print(matrix1)
                    print('Создание матрицы 2:')
                    matrix2 = create_matrix()
                    print('Матрицы созданы')
                    pass
                elif choice == 2:
                    print('Сложение матриц:', matrix1, ' + ', matrix2)
                    print('Результат:', matrix1 + matrix2)
                elif choice == 3:
                    print('Вычитание матриц:', matrix1, ' - ' , matrix2)
                    print('Результат:', matrix1 - matrix2)
                elif choice == 4:
                    # TODO: support vector multiplication
                    print('Введите вектор для умножения на матрицу')
                    vector = create_vector()
                    print('Умножение матрицы и вектора:', matrix1, ' * ', vector)
                    print('Результат:', matrix1 * vector)
                elif choice == 5:
                    print('Умножение матриц:', matrix1, ' * ', matrix2)
                    print('Результат:', matrix1 * matrix2)
                elif choice == 6:
                    print('Транспонирование:', matrix1, ' и ', matrix2)
                    print('Результат 1:', matrix1.transpose())
                    print('Результат 2:', matrix2.transpose())
                elif choice == 7:
                    print('Определитель матрицы 1:', matrix1)
                    print('Результат:', matrix1.determinant())
                    print('Определитель матрицы 2:', matrix2)
                    print('Результат:', matrix2.determinant())
                elif choice == 8:
                    print('Решение СЛАУ методом Гаусса:', matrix1)
                    print('Результат:', matrix1.gauss_equation())
                elif choice == 0:
                    run = False
                    if matrix1 is not None: del matrix1
                    if matrix2 is not None: del matrix2
                    print('Возврат в главное меню')
                else:
                    print('Некорректный ввод, попробуйте еще раз')
                    
                input('Нажмите Enter, чтобы продолжить...')
            except Exception as e:
                print('Ошибка:', e)
                input('Нажмите Enter, чтобы продолжить...')