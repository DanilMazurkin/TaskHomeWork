import good_info
import logging
from fileuser import FileUser

def main():
    """
    Main function with entry point
    """
    logging.basicConfig(filename="reporter.log", filemode='w', level=logging.INFO)

    info_list = good_info.GoodInfoList()
    fileuser = FileUser()
    file_data = fileuser.select_file()
    info_list.get_from_file(file_data)
    fileuser.save_by_directory()


    access_by_name = info_list["сушки 1кг."]
    logging.info("Доступ по ключу: ")
    logging.info(access_by_name)
    info_list.check_date_import_list()

    info_list.get_std()
    logging.info("Стандартное отколнение")
    logging.info(info_list.get_std())

    info_list.remove_last()
    logging.info("Количество элементов в списке товаров: ")
    logging.info(len(info_list))

    price_sort = info_list.sort("price")
    logging.info("\nСортировка по цене")

    for good in price_sort:
        logging.info(good)

    info_list.remove_expensive() 

    list_most_expensive = info_list.get_list_most_expensive()

    logging.info("\nСамые дорогие товары")

    for good in list_most_expensive:
        logging.info(good)

    logging.info("\nСамые дешевые товары")
    list_most_cheapset = info_list.get_list_with_cheap_goods()

    for good in list_most_cheapset:
        logging.info(good)

    logging.info("\nТовары которые заканчиваются")
    list_ending_goods = info_list.get_list_ending_goods()

    for good in list_ending_goods:
        logging.info(good)

    info_value = info_list.get_value_info()

    logging.info("Общее количество товаров:"
        " {amount} \n".format(amount=info_value['amount']))
    logging.info("Средняя цена товара: {mean} \n".format(mean=info_value['mean']))

    logging.info("Всего позиций товаров: "
        " {count} \n".format(count=len(info_list)))
    logging.info("Все товары: \n")
    logging.info(info_list)


if __name__ == '__main__':
    main()
