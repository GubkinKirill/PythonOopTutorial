# Магические методы __setattr__, __getattribute__, __getattr__, __delattr__
"""
* __setattr__(self, key, value) - автоматически вызывается при изменении свойсвтва key класса
* __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
* __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
* __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно существует оно или нет) 
"""
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_coords(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD and self.MIN_COORD <= y <= self.MAX_COORD:
            self.x = x
            self.y = y
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Запрещено получать значение x')
        else:
            return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError('Запрещено изменять значение ')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return f'Свойство {item} не существует'

    def __delattr__(self, item):
        object.__delattr__(self, item)

pt1 = Point(1, 2)
pt2 = Point(3, 4)  
print(pt1.yy)

del pt1.x
print(pt1.__dict__)