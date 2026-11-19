book = {}

while True:
    print("\n 1) Добави \n 2) Търси \n 3) Изтрий \n 0) Изход")
    choice = input("Избор: ")

    match choice:
        case '1':
            name = input("Име: ")
            book[name] = input("Телефон: ")
            print("Записано.")
        case '2':
            name = input("Име: ")
            print(book.get(name, "Няма такъв контакт."))
        case '3':
            name = input("Име: ")
            if book.pop(name, None) is None:
                print("Няма такъв контакт.")
            else:
                print("Изтрит.")
        case '0':
            break
        case _:
            print("Невалиден избор.")

print("\nВсички контакти:")
for name, phone in book.items():
    print(f"{name}: {phone}")