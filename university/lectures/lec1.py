import random

for x in range(1,101):
    print(x)

# Fibonacci
for x in range (1,101,2):
    print(x)

#----------------------------------
sum = 0
for i in range(3):
    x = int(input(f"[{i+1}]="))
    sum += x
print("sum=", sum)

numbers = int(input("How many numbers you want to sum? "))
sum = 0
for i in range(numbers):
    x = int(input(f"[{i+1}]="))
    sum += x
print("sum=",sum)

num = int(input("How many numbers you want to multiply? "))
mult = 1
for i in range(num):
    x = random.randrange(-10,10)
    print(x, end=" ")
    mult *= x
    print("\nmult=",mult)

sum = 0
min = 0
while True:
    x = int(input("x= "))
    if x == 0:
        break
    sum += x
    if min == 0 or min > x:
        min = x
    print("sum= ",sum,"min= ",min)


is_init = False
max_even = 0;
while True:
    x = int(input("x= "))
    if x==0:
        break
    if x % 2 == 0:
        if not is_init:
            max_even = x
            is_init = True
        elif max_even < x:
            max_even = x
    if is_init:
        print("max even = ", max_even)
    else:
        print("No such data...")
