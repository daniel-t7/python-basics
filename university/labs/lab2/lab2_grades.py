students = {}

def average(grades):
    total = 0
    for g in grades:
        total += g
    return total / len(grades) if grades else 0

while True:
    print("\n 1) Добави оценка \n 2) Среден успех \n 3) Справка \n 0) Изход")
    choice = input("Избор: ")

    match choice:
        case '1':
            name = input("Ученик: ")
            grade = float(input("Оценка: "))
            students.setdefault(name, []).append(grade)
        case '2':
            name = input("Ученик: ")
            if name in students:
                print(f"Среден успех: {average(students[name]):.2f}")
            else:
                print("Няма такъв ученик.")
        case '3':
            for name, grades in students.items():
                print(f"{name}: {average(grades):.2f}")
        case '0':
            break
        case _:
            print("Невалиден избор.")