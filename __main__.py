import good_info
import logging
from file_work import FileWork
from datetime import datetime
from db_worker import DB_Worker
import json


FORMAT = '%(asctime)s %(levelname)s %(filename)s - %(funcName)s - %(message)s'
    
logging.basicConfig(filename="reporter.log", filemode='a',
                    level=logging.INFO, format=FORMAT)

info_list = DB_Worker()
    
file_goods = FileWork()
file_data = file_goods.select_path_file()

file_goods.save_in_directory()

if len(file_data) > 0:
    info_list.get_from_file(file_data)
    info_list.remove("морковь 1кг")
    info_list.remove_expensive()
    deviation = info_list.get_std()
    info_value = info_list.get_value_info()

    print("Количество товаров: {amount} \n".format(
                                                amount=info_value['amount']))
    print("Средняя цена товара: {mean} \n".format(
                                                mean=info_value['mean']))
    print("Стандартное отколнение")
    print(deviation)
    info_list.remove_last()
    info_list.product_buy("соль 1 кг", 5)

    price_sort_goods = info_list.sort("price")
    print("\nСортировка по цене")

    for good in price_sort_goods:
        print("Имя: {name} Цена: {price}".format(
                                            name = good.name,
                                            price = good.price))

    info_list.remove_expensive() 

    list_most_expensive = info_list.get_list_most_expensive()

    print("\nСамые дорогие товары")

    for good in list_most_expensive:
        print("Имя: {name} Цена: {price}".format(
                                            name = good.name,
                                            price = good.price))

    print("\nСамые дешевые товары")
    list_most_cheapset = info_list.get_list_with_cheap_goods()

    for good in list_most_cheapset:
        print("Имя: {name} Цена: {price}".format(
                                            name = good.name,
                                            price = good.price))


    print("\nТовары которые заканчиваются")
    list_ending_goods = info_list.get_list_ending_goods()

    for good in list_ending_goods:
        print("Имя: {name} Цена: {price}".format(
                                            name = good.name,
                                            price = good.price))



