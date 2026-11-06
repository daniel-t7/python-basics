book = {}

while True:
    print("\n1) Добави \n 2) Търси \n 3) Изтрий \n 0) Изход")
    choice = input("Избор: ")

    if choice == "1":
        name = input("Име: ")
        book[name] = input("Телефон: ")
        print("Записано.")

    elif choice == "2":
        name = input("Име: ")
        print(book.get(name, "Няма такъв контакт."))

    elif choice == "3":
        name = input("Име: ")
        if book.pop(name, None) is None:
            print("Няма такъв контакт.")
        else:
            print("Изтрит.")

    elif choice == "0":
        break
    else:
        print("Невалиден избор.")

print("\nВсички контакти:")
for name, phone in book.items():
    print(f"{name}: {phone}")