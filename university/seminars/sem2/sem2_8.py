"""
Намерете броя на срещанията на подниза 'ab' в низа 'ab bc ab bd ab
be' и разменете знаците 'a' и 'b' във всеки случай . Покажете получения резултат
на екрана
"""
text = "ab bc ab bd ab be"
result = ""

for char in text:
    if char == "a":
        result += "b"
    elif char == "b":
        result += "a"
    else:
        result += char

print("Брой срещания:", text.count("ab"))
print("Резултат:", result)