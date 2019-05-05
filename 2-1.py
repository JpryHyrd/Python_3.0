"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных 
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание 
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения 
параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра 
поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, 
os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, 
main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», 
«Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data 
(также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение 
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
#без импората codecs выдавало ошибку:
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>
import codecs
import csv
def read(filee):
    name = codecs.open(filee, "r", "utf_8_sig")
    lst = []
    a = name.read()
    lst.append(a.split(", "))
    name.close()
    list = lst[0]
    main_data = []
    info = []
    for i in list:
        g = []
        r = str(i)
        g.append(r.split(" : "))
        main_data.append(g[0][0])
        info.append(g[0][1])
    return main_data, info

def get_data(file1, file2, file3):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    main_data, first = read(file1)
    main_data, second = read(file2)
    main_data, third = read(file3)

    os_prod_list.append(first[0])
    os_prod_list.append(second[0])
    os_prod_list.append(third[0])

    os_name_list.append(first[1])
    os_name_list.append(second[1])
    os_name_list.append(third[1])


    os_code_list.append(first[2])
    os_code_list.append(second[2])
    os_code_list.append(third[2])

    os_type_list.append(first[3])
    os_type_list.append(second[3])
    os_type_list.append(third[3])

    return main_data, first, second, third

def write_to_csv(csv_href):
    main_data, first, second, third = get_data("info_1.txt", "info_2.txt", "info_3.txt")
    end_list = [main_data, first, second, third]
    
    with open(csv_href, "w") as csvi:
        write_csv = csv.writer(csvi)
        for row in end_list:
            write_csv.writerow(row)
            
    with open(csv_href, "r") as csvi:
        print(csvi.read())
write_to_csv("any.csv")





