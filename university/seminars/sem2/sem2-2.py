"""
Напишете програма на Python, която създава списък от n въведени
от потребителя низа и извършва следните обработки: определя кой от
записаните в списъка низове е с най-голяма дължина, заменя търсен низ с друг
въведен от потребителя, изтрива избран низ и вмъква нов низ в избрана
позиция в списъка.
"""


count = int(input("count = "))

words = []

for i in range(count):
    word = input("Въведи низ: ")
    words.append(word)

# Най-дълъг низ
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Най-дългият е:", longest)

# замяна на низ
index = int(input("Кой да бъде заменен(по index): "))
new_word = input("Новия: ")

if 0 <= index < len(words):
    words[index] = new_word

print("След замяната:", words)

# изтриване
index = int(input("Кой да бъде изтрит: "))

if 0 <= index < len(words):
    del words[index]

print("След изтриването:", words)

# Вмъкване
new_word = input("Нов низ за вмъкване: ")
index = int(input("Индекс: "))

words.insert(index, new_word)

print("Краен списък:", words)