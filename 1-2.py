"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode
и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

a = b"class"
b = b"function"
c = b"method"

print()
print(a, end = "")
print("(len = " + str(len(a)) + ")", end = " - ")
print(type(a))

print()
print(b, end = "")
print("(len = " + str(len(b)) + ")", end = " - ")
print(type(b))

print()
print(c, end = "")
print("(len = " + str(len(c)) + ")", end = " - ")
print(type(c))


