# 1
count = int(input("count = "))
for n in range(count):
    n = int(input("n = "))

# 2
count = int(input("count = "))
sum = 0
for n in range(count):
    n = int(input("n = "))
    sum += n
print(sum)

# 3
n = int(input('n = '))
for i in range(1, n + 1):
    print("*" * i)

# 4
import math

n = int(input('n = '))

if n > 0:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} не е просто число.")
            break
    else:
        print(f"{n} е просто число.")
else:
    print(f"{n} не е просто число.")