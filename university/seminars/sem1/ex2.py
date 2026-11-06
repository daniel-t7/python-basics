"""
Да се напише програма за определяне на максималното четно число и
минимума на нечетните числа. в поредица от въведените от потребителя
числа. Да се определи и броя на четните числа и нечетните числа в
поредицата.
"""
counter = int(input('counter = '))
maxOdd = 0
minEven = 0
counterOdd = 0
counterEven = 0
for i in range(counter):
    i = int(input('i = '))
    if i % 2 != 0:
        if i > maxOdd:
            maxOdd = i
        counterOdd += 1
    elif i % 2 == 0:
        if i < minEven:
            minEven = i
        counterEven += 1

print(f'maxOdd = {maxOdd}, minEven = {minEven},\ncounterOdd = {counterOdd}, counterEven = {counterEven}')
