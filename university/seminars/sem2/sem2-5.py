"""
Напишете програма на Python, която създава речник от 7 въведени
от потребителя низа и съответстващите им цели числа и извършва следните
обработки: разпечатва съдържането на речника, определя на кой ключ
съответства най-голямото въведено цяло число от записаните в речника,
заменя стойността въведена за избран ключ с друга въведена от потребителя,
изтрива стойност от речника по нейния ключ и добавя нова стойност в речника
заедно с нейния ключ.
"""

dictionary = {}

for i in range(7):
    key = input("key = ")
    value = int(input("value = "))

    dictionary[key] = value

# извеждане
for key in dictionary:
    print(key, ":", dictionary[key])

# ключ с най-голяма стойност
max_key = max(dictionary, key=dictionary.get)

print("Max key: ", max_key)
print("Value of max key:", dictionary[max_key])

# промяна
key = input("Your key: ")
new_value = int(input("New value: "))

if key in dictionary:
    dictionary[key] = new_value

# изтриване
remove_key = input("Remove this key: ")

if remove_key in dictionary:
    del dictionary[remove_key]

# добавяне
key = input("New key: ")
value = int(input("New value: "))

dictionary[key] = value

print("Your Dictionary: ")

for key in dictionary:
    print(key, ":", dictionary[key])