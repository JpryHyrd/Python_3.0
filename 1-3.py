"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""
try:
    print(b"attribute")
except Exception:
    print("\"attribute\" невозможно записать в байтовом типе.")
print()
"""try:
    a = b"класс"
except Exception:
    print("\"класс\" невозможно записать в байтовом типе.")
print()
try:
    a = b"функция"
except Exception:
    print("\"функция\" невозможно записать в байтовом типе.")
print()"""
#Cлова класс и функция невозможно записать в байтовом типе, возникает SyntaxError
try:
    print(b"type")
except Exception:
    print("\"type\" невозможно записать в байтовом типе.")
    


