# the main difference between lists and tuples is that tuples are immutable
# immutable - once created they cannot be modified

items: tuple = 1, True, 'Text'
print(items)

coordinates: tuple[float,float] = 1.5, 2.5
print(coordinates)