import good_info
import logging
from file_work import FileWork


def main():
    """
    Main function with entry point
    """

    FORMAT = '%(asctime)s %(levelname)s %(filename)s - %(funcName)s - %(message)s'
    
    logging.basicConfig(filename="reporter.log", filemode='a',
                        level=logging.INFO, format=FORMAT)

    info_list = good_info.GoodInfoList()
    file_goods = FileWork()
    file_data = file_goods.select_path_file()

    file_goods.save_in_directory()

    if len(file_data) > 0:
        info_list.get_from_file(file_data)
        info_value = info_list.get_value_info()
        
        list_expensive = info_list.get_list_most_expensive()
        
        most_expensive_test = good_info.GoodInfoList()
        most_expensive_test.add(
                                good_info.GoodInfo("рыба мороженая, Кета 1кг", 
                                "400", "5", "2020-12-30", "90", "2020-12-30"))
        print(list_expensive)
        print(most_expensive_test)
        print(list_expensive == most_expensive_test)

        print("Количество товаров: {amount} \n".format(amount=info_value['amount']))
        print("Средняя цена товара: {mean} \n".format(mean=info_value['mean']))
        print("Количество товаров: {amount} \n".format(amount=info_value['amount']))
        print("Количество элементов в списке товаров: ")
        print("Стандартное отколнение")
        print(info_list.get_std())
        print(len(info_list))
        info_list.remove_last()


        info_list.product_buy("соль 1 кг", 5)
    
        info_list.check_date_manafucture_list()
        info_value = info_list.get_value_info()

        price_sort = info_list.sort("price")
        print("\nСортировка по цене")

        print(price_sort)

        info_list.remove_expensive() 

        list_most_expensive = info_list.get_list_most_expensive()
        print(list_most_expensive[0])

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

if __name__ == '__main__':
    main()
