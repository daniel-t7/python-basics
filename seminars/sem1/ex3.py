"""
Напишете програма, която проверява дали едно въведено от
потребителя число се намира в интервала [n; m].
"""
n = int(input('n = '))
m = int(input('m = '))
num = int(input('num = '))
isNumIn = False
for i in range(n, m):
   if num == i:
       isNumIn = True
print(isNumIn)