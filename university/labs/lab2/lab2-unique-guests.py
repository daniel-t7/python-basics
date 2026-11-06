names = ["Иван", "Мария", "Петър", "Иван", "Елена", "Мария", "Георги"]

unique = set(names)
print("Брой уникални гости:", len(unique))

name = input("Въведете име: ").strip()
if name in unique:
    print(f"{name} е поканен/а.")
else:
    print(f"{name} не е в списъка с гости.")