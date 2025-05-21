
class EquationSolver:
    def __init__(self, a, b, c = None):
        self._a = a
        self._b = b
        self._type = 'linear'
        if (c is not None):
            self._type = 'quadratic'
            self._c = c

    def __str__(self):
        if self._type == 'linear':
            return f'{self._a}x + {self._b} = 0'
        elif self._type == 'quadratic':
            return f'{self._a}x^2 + {self._b}x + {self._c} = 0'
        else:
            return 'Неизвестный тип уравнения'

    def solve(self):
        if self._type == 'linear':
            return self.solve_linear(self._a, self._b)
        elif self._type == 'quadratic':
            return self.solve_quadratic(self._a, self._b, self._c)
        else:
            raise ValueError("Неизвестный тип уравнения")

    def solve_linear(self, a, b):
        if a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен нулю.")
        return -b / a

    def solve_quadratic(self, a, b, c):
        if a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен нулю в квадратном уравнении.")

        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("Уравнение не имеет действительных корней.")

        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)

        return x1, x2