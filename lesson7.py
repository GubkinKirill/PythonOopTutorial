# Режимы доступа public, private, protected. Сеттеры и геттеры
'''
* attribute (без одного или двух подчеркиваний) - public(публичный атрибут)
* _attribute (с одним подчеркиванием) - protected(защищенный атрибут), доступ к атрибуту только внутри класса и его наследников
* __attribute (с двумя подчеркиваниями) - private(приватный атрибут), доступ к атрибуту только внутри класса
'''


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, value):
        if type(value) in (int, float):
            return True
        return False
    
    def set_coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')
        
    def get_coords(self):
        return self.__x, self.__y

pt = Point(1, 2)
pt.set_coords(3, 4)
print(pt.get_coords()) # (3, 4)
print(pt._Point__x) # 3 - доступ к приватному атрибуту
print(pt.__x) # AttributeError: 'Point' object has no attribute '__x'
print(pt.__y) # AttributeError: 'Point' object has no attribute '__y'

