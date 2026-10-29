"""
Да се напише програма, която преброява числата със стойност в избрани
от потребителя граници в поредица от числа. Да се определи и сумата на
числата, лежащи в зададения от потребителя интервал.
"""
n = int(input("n = "))

a = int(input("a = "))
b = int(input("b = "))

count = 0
sum = 0

for i in range(n):
    num = int(input("num = "))

    if a <= num <= b:
        count += 1
        sum += num

print("count = ", count)
print("sum = ", sum)