tasks = []


def show_tasks():
    if not tasks:
        print("Списъкът е празен")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")


while True:
    print("\n 1) Добави \n 2) Изтрий \n 3) Редактирай \n 4) Принт \n 0) Изход")
    choice = input("Избор: ")

    match choice:
        case '1':
            tasks.append(input("Нова задача: "))
        case '2':
            key = input("Индекс или име: ")
            if key in tasks:
                tasks.remove(key)
                print("Изтрихте: ", key)
            elif key.isdigit():
                print("Изтрихте:", tasks.pop(int(key) - 1))
        case '3':
            show_tasks()
            index = input("Задача: ")
            if index.isdigit():
                tasks[int(index) - 1] = input("Нов текст: ")
        case '4':
            show_tasks()
        case '0':
            break
        case _:
            print("Невалиден избор.")