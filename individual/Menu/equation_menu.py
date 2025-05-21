import os

from MyMath.EquationSolver import EquationSolver


def matrices_menu():
        run = True
        solver = EquationSolver()
        while run:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Работа с уравнениями')
                print('1. Решить уравнение 1-й степени')
                print('2. Решить уравнение 2-й степени')
                print('3. Решить систему линейных уравнений')
                print('0. Вернуться в главное меню')

                choice = int(input('Выберите пункт меню: '))

                match choice:
                    case 1:
                        print('Введите коэффициенты уравнения ax + b = 0')
                        a = float(input('a: '))
                        b = float(input('b: '))
                        equation = EquationSolver(a, b)
                        print('Уравнение:', equation)
                        result = equation.solve()
                        # result = solver.solve_linear(a, b)
                        # print(f'Решение уравнения {a}x + {b} = 0: x = {result}')
                    case 2:
                        print('Введите коэффициенты уравнения ax^2 + bx + c = 0')
                        a = float(input('a: '))
                        b = float(input('b: '))
                        c = float(input('c: '))
                        result = solver.solve_quadratic(a, b, c)
                        print(f'Решение уравнения {a}x^2 + {b}x + {c} = 0: x1 = {result[0]}, x2 = {result[1]}')
                    case 3:
                        print('Вычитание матриц:', matrix1, ' - ' , matrix2)
                        print('Результат:', matrix1 - matrix2)
                    case 0:
                        run = False
                        if 'matrix1' in locals(): del matrix1
                        if 'matrix2' in locals(): del matrix2
                        print('Возврат в главное меню')
                    case _:
                        print('Некорректный ввод, попробуйте еще раз')

                input('Нажмите Enter, чтобы продолжить...')
            except Exception as e:
                print('Ошибка:', e)
                input('Нажмите Enter, чтобы продолжить...')