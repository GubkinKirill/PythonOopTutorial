# Дескрипторы (data descriptor и non-data descriptor)
# Дескрипторы - это объекты, которые управляют доступом к атрибутам класса.

class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise ValueError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._xr = x  # Устанавливаем значение для xr

p = Point3D(1, 2, 3)
print(p.xr, p.__dict__)  # 1 {'_x': 1, '_y': 2, '_z': 3, '_xr': 1}
p.xr = 10
print(p.xr, p.__dict__)  # 10 {'_x': 1, '_y': 2, '_z': 3, '_xr': 10}