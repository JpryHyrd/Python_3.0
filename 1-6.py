"""6. Создать текстовый файл test_file.txt, заполнить его 
тремя строками: «сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. Принудительно открыть 
файл в формате Unicode и вывести его содержимое."""
import locale
coding = locale.getdefaultlocale
print("Кодировка файла по умолчанию - ", end = "")
print(coding)

text = open("test_file.txt", "w")
text.write("Сетевое программирование\n")
text.write("Сокет\n")
text.write("Декоратор")
text.close()

text = open ("test_file.txt", encoding="utf-8", mode="r")
for i in text:
    print(i)
text.close()
#При попытке чтения файла возникает ошбка:
"""
Traceback (most recent call last):
  File "1-6.py", line 17, in <module>
    for i in text:
  File "C:\Program Files\Python37\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd1 in position 0: invalid continuation byte
"""




