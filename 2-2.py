"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), 
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в 
файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json
def write_order_to_json(json_href):
    item = input("Type name of item: ")
    quantity = int(input("Type count of this item: "))
    price = int(input("Price of this item: "))
    buyer = input("Buyer: ")
    date = input("Date(03.05.2019): ")

    json_dict = {
        "item" : item,
        "quantity" : quantity,
        "price" : price,
        "buyer" : buyer,
        "date" : date
    }
    
    with open(json_href, "w") as jswr:
        json.dump(json_dict, jswr, indent=4)
    obj = json.load(open(json_href))
    print(obj)

write_order_to_json("anny.json")











