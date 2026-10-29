"""
Да се напише програма, която намира сумата и средноаритметичната
стойност на четните и на нечетните числа в поредицата от въведените от
потребителя числа.
"""
count = int(input('count = '))
sumEven = 0
sumOdd = 0
avgEven = 0
avgOdd = 0
for i in range(count):
    i = int(input('i = '))
    if i % 2 == 0:
        sumEven += i
        avgEven = sumEven / 2
    elif i % 2 != 0:
        sumOdd += i
        avgOdd = sumOdd / 2

print(f'Odd Sum: {sumEven}')
print(f'Even Avg: {avgEven}')
print(f'Odd Sum: {sumOdd}')
print(f'Odd Avg: {avgOdd}')


