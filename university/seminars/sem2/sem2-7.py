"""
Да се напише програма, която създава речник с думи на английски
език и техния превод на български и извършва действия с него. Действията
включват: добавяне и изтриване на дума, извеждане на речника, търсене на
дума в речника и сортиране на думите в речника
"""

dictionary = {}

while True:
    print("1. Добавяне")
    print("2. Изтриване")
    print("3. Извеждане")
    print("4. Търсене")
    print("5. Сортиране")
    print("0. Изход")

    choice = int(input("Избери: "))

    match choice:
        case 1:
            english = input("Англ. дума: ")
            bulgarian = input("Бълг. превод: ")
            dictionary[english] = bulgarian
        case 2:
            english = input("Дума за изтриване: ")
            if english in dictionary:
                del dictionary[english]
        case 3:
            for english in dictionary:
                print(english, "-", dictionary[english])
        case 4:
            english = input("Дума за търсене: ")
            if english in dictionary:
                print("Превод:", dictionary[english])
            else:
                print("Думата не е намерена.")
        case 5:
            dictionary = dict(sorted(dictionary.items()))
            print("Сортиран речник:")
            for english in dictionary:
                print(english, "-", dictionary[english])
        case 0:
            break
