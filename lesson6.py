# Методы класса (classmethod) и статические методы (staticmethod)
# Методы класса (classmethod) - это методы, которые принимают первым аргументом класс, а не экземпляр класса
# Статические методы (staticmethod) - это методы, которые не принимают ни класс, ни экземпляр класса

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x**2 + y**2

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y





v = Vector(1, 222)
res = v.get_coords()
print(res)
print(Vector.validate(1))
print(v.validate(1))

print(Vector.norm2(3, 4))