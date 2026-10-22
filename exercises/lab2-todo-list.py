tasks = []


def showTaks():
    if not tasks:
        print("Списъкът е празен")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")


while True:
    print("\n 1) Добави \n 2) Изтрий \n 3) Редактирай \n 4) Принт \n 0) Изход")
    choice = input("Избор: ")
    if choice == "1":
        tasks.append(input("Нова задача: "))
    elif choice == "2":
        key = input("Индекс или име: ")
        if key in tasks:
            tasks.remove(key)
            print("Изтрихте: ", key)
        elif key.isdigit():
            print("Изтрихте:", tasks.pop(int(key) - 1))
    elif choice == "3":
        showTaks()
        index = input("Задача: ")
        if index.isdigit() and 1 <= int(index) <= len(tasks):
            tasks[int(index) - 1] = input("Нов текст: ").strip()

    elif choice == "4":
        showTaks()
    elif choice == "0":
        break;
    else:
        print("Това не от зададените числа.")


