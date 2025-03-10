# Паттерн "Моносостояние" (Monostate)
# Моносостояние - это паттерн проектирования, который обеспечивает
# совместимость с паттерном "Одиночка", но при этом позволяет создавать
# несколько экземпляров класса, которые будут иметь общее состояние.
# При этом каждый экземпляр класса может изменять это состояние, но
# все остальные экземпляры будут видеть эти изменения.


class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1

    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs

th1 = ThreadData()

th2 = ThreadData()

print(th1.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 1}
print(th2.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 1}

th2.id = 2

print(th1.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 2}
print(th2.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 2}

th1.new_attr = 'new'
print(th1.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 2, 'new_attr': 'new'}
print(th2.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 2, 'new_attr': 'new'}

