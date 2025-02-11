# Инициализатор __init__ и финализатор __del__ 
'''
__имя магического метода__

__init__(self) - инициализатор объекта класса
__del__(self) - финализатор класса
'''

class Point:
    color = 'red'
    circle = 2
    def __init__(self, x = 0, y = 0):
        print('вызов инит')
        self.x = x
        self.y = y
    
    def __del__(self):
        print('вызов деструктора ' + str(self))

    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self):
        return(self.x, self.y)

pt = Point(1, 2)
print(pt.__dict__)