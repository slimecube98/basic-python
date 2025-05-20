from MyMath.Vector import Vector

class Matrix:
    def __init__(self, rows):
        # Validate the matrix
        if not all(isinstance(item, (int, float)) for row in rows for item in row):
            raise TypeError("Все элементы матрицы должны быть числами (int или float)")

        if not all(len(row) == len(rows[0]) if rows else 0 for row in rows):
            raise ValueError("Каждая строка матрицы должна иметь одинаковую длину")
        
        self._rows = rows
        self._width = len(rows[0]) if rows else 0

        self._width = len(rows[0]) if rows else 0
        self._height = len(rows)
        self._is_quadratic = self._width == self._height

    @property
    def rows(self):
        return self._rows

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def is_quadratic(self):
        return self._is_quadratic
    
    def __del__(self):
        print("Matrix deleted")
        del self._rows

    def __str__(self):
        return "\n|" +  "\n|".join([" ".join(map(str, row))  + "|" for row in self._rows]) + "\n"
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Unsupported operand type(s) for +: 'Matrix' and '{}'".format(type(other).__name__))
        if self.width != other.width or self.height != other.height:
            raise ValueError("Для сложения матриц они должны иметь одинаковые размеры")
        
        return Matrix([[self.rows[i][j] + other.rows[i][j] for j in range(self.width)] for i in range(self.height)])
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Unsupported operand type(s) for -: 'Matrix' and '{}'".format(type(other).__name__))
        if self.width != other.width or self.height != other.height:
            raise ValueError("Для вычитания матриц они должны иметь одинаковые размеры")
        
        return Matrix([[self.rows[i][j] - other.rows[i][j] for j in range(self.width)] for i in range(self.height)])
    
    #TODO: support vector multiplication
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self.rows[i][j] * other for j in range(self.width)] for i in range(self.height)])
        elif isinstance(other, Vector):
            if self.width != 2:
                raise ValueError("Матрица должна быть 2x2 для умножения на вектор")
            return Vector([self.rows[0][0] * other.x + self.rows[0][1] * other.y, self.rows[1][0] * other.x + self.rows[1][1] * other.y])
        elif isinstance(other, Matrix):
            if self.width != other.height:
                raise ValueError("Матрицы должны иметь совместимые размеры для умножения")
            
            return Matrix([[sum(self.rows[i][k] * other.rows[k][j] for k in range(self.width)) for j in range(other.width)] for i in range(self.height)])
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Matrix' and '{}'".format(type(other).__name__))
        
    def determinant(self):
        if not self.is_quadratic:
            raise ValueError("Определитель можно вычислить только для квадратной матрицы")
        
        if self.width == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]
        
        det = 0
        for c in range(self.width):
            det += ((-1) ** c) * self.rows[0][c] * self.minor(0, c).determinant()
        return det
    
    def gauss_equation(self):
        """
        Решает СЛАУ для расширенной матрицы [A|b] методом Гаусса.
        Последний столбец считается вектором правых частей.
        Возвращает список решений x.
        """
         
        n = self.height
        m = self.width
        if m != n + 1:
            raise ValueError("Для расширенной матрицы число столбцов должно быть на 1 больше числа строк")
        # Копируем расширенную матрицу
        a = [self.rows[i][:] for i in range(n)]

        # Прямой ход
        for i in range(n):
            max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
            if abs(a[max_row][i]) < 1e-12:
                raise ValueError("Система не имеет единственного решения (нулевой столбец)")
            a[i], a[max_row] = a[max_row], a[i]
            pivot = a[i][i]
            a[i] = [x / pivot for x in a[i]]
            for j in range(i + 1, n):
                factor = a[j][i]
                a[j] = [a[j][k] - factor * a[i][k] for k in range(m)]

        # Обратная подстановка
        x = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = a[i][n] - sum(a[i][j] * x[j] for j in range(i + 1, n))
        return x

    def transpose(self):
        return Matrix([[self.rows[j][i] for j in range(self.height)] for i in range(self.width)])