import good_info
import logging
from work_with_file import Work_with_file


def main():
    """
    Main function with entry point
    """
    logging.basicConfig(filename="reporter.log", filemode='w', level=logging.INFO)

    info_list = good_info.GoodInfoList()
    work_with_file = Work_with_file()
    file_data = work_with_file.select_path_file()
    work_with_file.save_by_directory()

    if len(file_data) > 0:
        info_list.get_from_file(file_data)
        
        access_by_name = info_list["сушки 1кг."]
        print("Доступ по ключу: ")
        print(access_by_name)
        info_list.check_date_import_list()

        info_list.get_std()
        print("Стандартное отколнение")
        print(info_list.get_std())

        info_list.remove_last()
        print("Количество элементов в списке товаров: ")
        print(len(info_list))

        price_sort = info_list.sort("price")
        print("\nСортировка по цене")

        for good in price_sort:
            print(good)

        info_list.remove_expensive() 

        list_most_expensive = info_list.get_list_most_expensive()

        print("\nСамые дорогие товары")

        for good in list_most_expensive:
            print(good)

        print("\nСамые дешевые товары")
        list_most_cheapset = info_list.get_list_with_cheap_goods()

        for good in list_most_cheapset:
            print(good)

        print("\nТовары которые заканчиваются")
        list_ending_goods = info_list.get_list_ending_goods()

        for good in list_ending_goods:
            print(good)

        info_value = info_list.get_value_info()

        print("Общее количество товаров:"
            " {amount} \n".format(amount=info_value['amount']))
        print("Средняя цена товара: {mean} \n".format(mean=info_value['mean']))
        print("Всего позиций товаров: "
            " {count} \n".format(count=len(info_list)))
        print("Все товары: \n")
        print(info_list)


if __name__ == '__main__':
    main()
