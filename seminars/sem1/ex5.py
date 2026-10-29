"""
Напишете програма на Python, която n цели числа повдига на избрана
степен. Броят, всички числа и техните степени се въвеждат от
потребителя.
"""

n = int(input("n = "))

for i in range(n):
    num = int(input("num = "))
    stepen = int(input("stepen = "))

    rez = num ** stepen

    print(num, "на степен", stepen, "=", rez)