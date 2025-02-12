# Магический метод __new__. Пример паттерна Singleton
# __new()__ - вызывается перед созданием объекта класса 

class Point:
    def __new__(cls, *args, **kwargs):
        print('Вызов  __new__ для ' + str(cls))
# cls ссылается на класс
# self ссылается на экземпляр класса
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print('вызов __init__ для ', str(self))

pt = Point(1, 2)


        
