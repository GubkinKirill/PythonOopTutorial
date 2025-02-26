# Методы классов. Параметр self

'''
self - в Python это не метод, а специальный параметр, который передается первым аргументом в метод класса и представляет собой 
ссылку на экземпляр класса. Он используется для доступа к атрибутам и методам экземпляра из методов класса
'''
class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self):
        return(self.x, self.y)

#
pt = Point()
pt2 = Point()
pt.set_coords(1, 2)
pt2.set_coords(10, 20)
print(pt.__dict__)
print(pt2.__dict__)

print(pt.get_coords())
print(pt2.get_coords())