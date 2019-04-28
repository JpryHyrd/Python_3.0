"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
преобразовать строковые представление в формат Unicode и также провтериь тип и содержимое переменных.
"""
a = "разработка"
b = "сокет"
c = "декоратор"
print(a, "-", end = " ")
print(type(a))
print(b, "-", end = " ")
print(type(b))
print(c, "-", end = " ")
print(type(c))

a1 = a.encode("utf-8")
print("\n" + a, "-", end = " ")
print(a1)
print(type(a1))

b1 = b.encode("utf-8")
print("\n" + b, "-", end = " ")
print(b1)
print(type(b1))

c1 = c.encode("utf-8")
print("\n" + c, "-", end = " ")
print(c1)
print(type(c1))

