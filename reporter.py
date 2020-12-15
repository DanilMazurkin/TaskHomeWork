import good_info

if __name__ == '__main__':
    info_list = good_info.GoodInfoList()
    list_goods = info_list.get_from_file("goods2.info")
    info_list.add_goods_in_list(list_goods)
    info_list.get_std()
    info_list.remove_last()
    price_sort = info_list.sort("price")
    print("Количество элементов в списке товаров: ", len(info_list))
    print("Стандартное отколнение")
    print(info_list.get_std())
    print("\nСортировка по цене")

    for good in price_sort:
        print(good)

    info_list.remove_expensive() 
    list_most_expensive = info_list.get_list_most_expensive()
    list_most_cheapset = info_list.get_list_with_cheap_goods()
    list_ending_goods = info_list.get_list_ending_goods()

    print("\nСамые дорогие товары")

    for good in list_most_expensive:
        print(good)

    print("\nСамые дешевые товары")

    for good in list_most_cheapset:
        print(good)

    print("\nТовары которые заканчиваются")

    for good in list_ending_goods:
        print(good)

    info_value = info_list.get_value_info()

    print("Общее количество товаров:"
        " {amount} \n".format(amount=info_value['amount']))
    print("Средняя цена товара: {mean} \n".format(mean=info_value['mean']))

    print("Всего позиций товаров: "
        " {count} \n".format(count=len(info_list)))

    for good in info_list:
        print(good)

    # для удобства вывода, чтобы не городить циклы
    # лучше переопределить __str__() в GoodInfoList
    print(info_list)
