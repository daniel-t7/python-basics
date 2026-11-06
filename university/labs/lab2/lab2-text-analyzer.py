text = input("Въведете изречение: ")
word = input("Търсена дума: ")

t,w = text.lower(),word.lower()

if w in t:
    print("Брой срещания:", t.count(w))
    print("Първа позиция (индекс):", t.find(w))
else:
    print("Думата не се съдържа в текста.")
