
class Vector:
    def __init__(self, coordinates):
        if len(coordinates) != 2:
            raise ValueError("У вектора должно быть 2 координаты")
        
        if not all(isinstance(coord, (int)) for coord in coordinates):
            raise TypeError("Все координаты вектора должны быть числами (int)")

        self._coordinates = coordinates

    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value

    @property
    def x(self):
        return self._coordinates[0]

    @property
    def y(self):
        return self._coordinates[1]
    
    def __del__(self):
        print("Vector({}, {}) deleted".format(self.x, self.y))
        del self._coordinates
    
    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def length(self):
        return (pow(self.x, 2) + pow(self.y, 2)) ** .5
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([self.x * other, self.y * other])
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(other).__name__))
        
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))
        return Vector([self.x + other.x, self.y + other.y])
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type(s) for -: 'Vector' and '{}'".format(type(other).__name__))
        return Vector([self.x - other.x, self.y - other.y])
    
    def angle_between(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type(s) for angle_between: 'Vector' and '{}'".format(type(other).__name__))
        if self.length() == 0 or other.length() == 0:
            raise ValueError("Невозможно вычислить угол между нулевыми векторами")
        
        vectors_product = self * other
        if vectors_product == 0:
            raise ValueError("Угол между векторами равен 90 градусов")
        
        # можно использовать math.acos чтобы получить угол в радианах
        # + можно использовать math.degrees чтобы получить угол в градусах

        return vectors_product / (self.length() * other.length())
    
    def is_collinear_with(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type(s) for is_collinear_with: 'Vector' and '{}'".format(type(other).__name__))
        if self.length() == 0 or other.length() == 0:
            raise ValueError("Невозможно проверить коллинеарность с нулевыми векторами")
        
        return self.x/other.x == self.y/other.y