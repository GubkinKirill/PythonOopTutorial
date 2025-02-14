# Магические методы __setattr__, __getattribute__, __getattr__, __delattr__
"""
* __setattr__(self, key, value)__ - автоматически вызывается при изменении свойсвтва key класса

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
    @classmethod
    def set_bound(cls, left):
        cls.MAX_COORD = left

pt1 = Point(1, 2)
pt2 = Point(3, 4)  
print(pt1.MAX_COORD) # 100
print(pt2.MAX_COORD) # 100

pt1.set_bound(50)
print(pt1.MAX_COORD) # 50
print(Point.MAX_COORD) # 50

