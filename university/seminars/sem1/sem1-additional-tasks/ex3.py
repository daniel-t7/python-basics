"""
3.L. Даден е списък, съдържащ дублиращи се елементи ["Apple", "Banana", "Apple", "Orange", "Grape", "Banana", "Kiwi", "Orange"].
Напишете програма, която създава нов списък с уникалните елементи, запазвайки реда на първото им появяване.
"""

fruits = ["Apple", "Banana", "Apple", "Orange", "Grape", "Banana", "Kiwi", "Orange"]
uniqueFruits = list(dict.fromkeys(fruits))

print(uniqueFruits)