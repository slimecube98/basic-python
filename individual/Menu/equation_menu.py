import os

from MyMath.EquationSolver import EquationSolver

def create_equation():
    print('Введите коэффициенты уравнения ax + b = 0')
    a = float(input('a: '))
    b = float(input('b: '))
    return EquationSolver(a, b)

def create_quadratic_equation():
    print('Введите коэффициенты уравнения ax^2 + bx + c = 0')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    return EquationSolver(a, b, c)

def matrices_menu():
        run = True
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
                        equation = create_equation()
                        result = equation.solve()
                        print(f'Решение уравнения {equation}: x = {result}')
                    case 2:
                        equation = create_quadratic_equation()
                        x1, x2 = equation.solve()
                        print(f'Решение уравнения {equation}: x1 = {x1}, x2 = {x2}')
                    case 3:
                        # we need 3 quadratic equations to solve a system of linear equations
                        print('Введите коэффициенты для системы линейных уравнений:')
                        eq1 = create_quadratic_equation()
                        eq2 = create_quadratic_equation()
                        eq3 = create_quadratic_equation()
                        
                        result = eq1.solve_gauss(eq2, eq3)
                        print(f'Решение системы уравнений:\n{eq1}\n{eq2}\n{eq3}\nРезультат: {result}')

                    case 0:
                        run = False
                        print('Возврат в главное меню')
                    case _:
                        print('Некорректный ввод, попробуйте еще раз')

                input('Нажмите Enter, чтобы продолжить...')
            except Exception as e:
                print('Ошибка:', e)
                input('Нажмите Enter, чтобы продолжить...')