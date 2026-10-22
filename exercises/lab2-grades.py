students = {}

def average(grades):
    total = 0
    for g in grades:
        total += g
    return total / len(grades) if grades else 0

while True:
    print("\n1) Добави оценка \n 2) Среден успех \n 3) Справка \n 0) Изход")
    choice = input("Избор: ")

    if choice == "1":
        name = input("Ученик: ")
        grade = float(input("Оценка: "))
        students.setdefault(name, []).append(grade)

    elif choice == "2":
        name = input("Ученик: ")
        if name in students:
            print(f"Среден успех: {average(students[name]):.2f}")
        else:
            print("Няма такъв ученик.")

    elif choice == "3":
        for name, grades in students.items():
            print(f"{name}: {average(grades):.2f}")

    elif choice == "0":
        break
    else:
        print("Невалиден избор.")