"""
Да се напише програма, която създава две множества от m цели
числа, въведени от клавиатурата и извършва следните операции с тях:
определя размера на двете създадени множества, обединение на двете
множества, разлика на двете множества, пресичане на двете множества,
премахване на избран елемент от първо множество и изчистване на двете
множества.
"""

m = int(input("count = "))

set1 = set()
set2 = set()

for i in range(m):
    num = int(input("num set 1 = "))
    set1.add(num)

for i in range(m):
    num = int(input("num set 2 = "))
    set2.add(num)

# размер
print("set 1 size: ", len(set1))
print("set 2 size: ", len(set2))

# обединение
print("обединение:", set1 | set2)

# разлика
print("разлика:", set1 - set2)

# пресичане
print("пресичане:", set1 & set2)

# премахване на елемент
remove_number = int(input("remove this number: "))

if remove_number in set1:
    set1.remove(remove_number)

print("Първо множество:", set1)

# изчистване
set1.clear()
set2.clear()

print("set 1 cleared: ", set1)
print("set 2 cleared: ", set2)