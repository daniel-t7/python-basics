"""
Напишете програма, която намира сумата и произведението само от
положителните числа в поредица от въведени от потребителя стойности.
Използвайте стойност -99 за край на въвеждането.
"""
sum = 0
proizvedenie = 1

while True:
    num = int(input("num = "))

    if num == -99:
        break

    if num > 0:
        sum += num
        proizvedenie *= num

print("sum = ", sum)
print("proizvedenie = ", proizvedenie)