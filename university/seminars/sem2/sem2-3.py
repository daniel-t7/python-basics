"""
Да се напише програма, която въвежда m низа за ключ и m цели
числа за стойност от клавиатурата и ги записва в речник. Програмата да
извърши следните обработки: търси избран ключ в речника, променя
стойността на елемент от речника по неговия ключ, изтрива елемент от
речника по ключ, извежда всички ключове от речника, извежда всички
стойности от речника, сортира речника по ключове. Извеждането на
съдържанието на речника да се прави с обхождане на елементите му по ключ
"""

m = int(input("count = "))

dictionary = {}

for i in range(m):
    key = input("key: ")
    value = int(input("value: "))

    dictionary[key] = value

# търсене на ключ
search_key = int(input('Your key: '))

if search_key in dictionary:
    print('Има го.')
else:
    print('Нема го.')

# промяна на стойност
key = int(input('Your key: '))
new_value = int(input("New value: "))
if key in dictionary:
    dictionary[key] = new_value

# изтриване
key = input("ключ за изтриване: ")

if key in dictionary:
    del dictionary[key]

# всички ключове
print("ключове: ")
for кеу in dictionary:
    print(key)

# Всички стойности
print("стойности:")

for value in dictionary.values():
    print(value)

# Сортиране по ключове
sorted_dictionary = dict(sorted(dictionary.items()))

print("Сортиран речник:")

for key in sorted_dictionary:
    print(key, ":", sorted_dictionary[key])
