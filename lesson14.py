# Магические методы __str__, __repr__, __len__ и __abs__

# Магический метод __str__
# Метод __str__ вызывается функцией str() для получения строкового представления объекта.

# Магический метод __repr__
# Метод __repr__ вызывается функцией repr() для получения строкового представления объекта.


class Cat:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__name}'
    def __repr__(self):
        return f'{self.__class__} {self.__name}'
    

c = Cat('Мурзик')
print(str(c))  # Мурзик
print(repr(c))  # <__main__.Cat object at 0x7f3e3b0c2b80>
print(c)  # Мурзик

# Магический метод __len__
# Метод __len__ вызывается функцией len() для получения длины объекта.

# Магический метод __abs__
# Метод __abs__ вызывается функцией abs() для получения абсолютного значения объекта.


class Point:
    def __init__(self, *args):
        self.__coords = args
    def __len__(self):
        return len(self.__coords)
    def __abs__(self):
        return list(map(abs, self.__coords))
p = Point(1, -2, 3)
print(len(p))  # 3
print(abs(p))  # [1, 2, 3]