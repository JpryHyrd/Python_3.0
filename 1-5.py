"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице."""
import subprocess
args1 = ["ping", "yandex.ru"]
args2 = ["ping", "youtube.com"]

sub_ping1 = subprocess.Popen(args1, stdout=subprocess.PIPE)
sub_ping2 = subprocess.Popen(args2, stdout=subprocess.PIPE)

for i in sub_ping1.stdout:
    print(i)
    i = i.decode("cp866").encode("utf-8")
    print(i.decode("utf-8"))

for i in sub_ping2.stdout:
    print(i)
    i = i.decode("cp866").encode("utf-8")
    print(i.decode("utf-8"))




