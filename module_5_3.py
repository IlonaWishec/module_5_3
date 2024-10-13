class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, int(new_floor + 1)):
            if new_floor > self.number_of_floors or new_floor == 0:
                print('Такого этажа не существует')
                break
            else:
                print(i)

    def __len__(self):
        return int(self.number_of_floors)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10.
print(h2)  # Название: ЖК Акация, кол-во этажей: 20.
print(h1 == h2)  # __eq__ False
h1 = h1 + 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True
h1 += 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30.
h2 = 10 + h2
print(h2)
print(h1 > h2) # __gt__ # False
print(h1 >= h2) # __ge__ # True
print(h1 < h2) # __lt__ # False
print(h1 <= h2) # __le__ # True
print(h1 != h2) # __ne__ # False
