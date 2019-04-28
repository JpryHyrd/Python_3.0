"""4. Преобразовать слова «разработка», «администрирование», «protocol», 
«standard» из строкового представления в байтовое и выполнить обратное 
преобразование (используя методы encode и decode)."""

a = "разработка"
b = "администрирование"
c = "protocol"
d = "standard"


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

d1 = d.encode("utf-8")
print("\n" + d, "-", end = " ")
print(d1)
print(type(d1))

print()
a2 = a1.decode()
print(a1, end = " - ")
print(a2)
print(type(a2))

print()
b2 = b1.decode()
print(b1, end = " - ")
print(b2)
print(type(b2))

print()
c2 = c1.decode()
print(c1, end = " - ")
print(c2)
print(type(c2))

print()
d2 = d1.decode()
print(d1, end = " - ")
print(d2)
print(type(d2))



