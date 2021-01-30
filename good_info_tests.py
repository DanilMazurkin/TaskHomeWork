import os
import json
import logging
import good_info
import collections
from good_info import GoodInfoList
from good_info import GoodInfo
from execute_from_config import exec_function
from good_info import GoodInfo
from db_worker import DB_Worker
import unittest
from file_work import FileWork
from db_models import Good


class GoodInfoListTest(unittest.TestCase):

    def form_expensive_list_goods(self):
        """
        Function form list with most expensive goods
        :return: function return GoodInfoList with
        most expensive sort goods
        """ 

        self.database.truncate_all_tables()

        self.database.add(GoodInfo("рыба мороженая, Кета 1кг", 
                         "400", "5", "2020-12-30", "90", "2020-12-30"))
        
        most_expensive_test_list = self.database.get_all_goods()


        return most_expensive_test_list

    def form_cheapset_list_goods(self):
        """
        Function form list with cheapset goods
        :return: function return GoodInfoList with
        most cheapset sort goods
        """
        
        self.database.truncate_all_tables()

        list_with_object_cheapset_test = [
            GoodInfo('макароны Макфа,спагетти', '30', '10','2020-12-30', '360', '2020-12-30'),
            GoodInfo('макароны Макфа,рожки', '30', '7','2020-12-30', '360', '2020-12-30')
        ]
        
        for good in list_with_object_cheapset_test:
            self.database.add(good)

        most_cheapset_test_list = self.database.get_all_goods()

        return most_cheapset_test_list

    def form_ending_list_goods(self):
        """
        Function form list with ending goods
        :return: function return GoodInfoList with
        most ending sort goods
        """
        
        self.database.truncate_all_tables()

        list_with_objects_ending_test = [
            GoodInfo('вермишель Макфа 1кг', '45', '2','2020-12-30', '720', '2020-12-30')
            # GoodInfo('вермишель Макфа 1кг', '2', '45','2020-12-30', '720', '2020-12-30')
        ]

        for good in list_with_objects_ending_test:
            self.database.add(good)

        list_with_ending_goods = self.database.get_all_goods()

        return list_with_ending_goods

    def form_sort_amount_list(self):
        """
        Function form list with amount goods
        :return: function return GoodInfoList with
        amount sort goods
        """

        sort_amount_list = [
            GoodInfo('вермишель Макфа 1кг', '45', '2','2020-12-30', '720', '2020-12-30'),
            GoodInfo('рыба мороженая, Кета 1кг', '400', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Окунь 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Треска 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Горбуша 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('макароны Макфа,рожки', '30', '7','2020-12-30', '360', '2020-12-30'),
            GoodInfo('рис круглозерный 1кг', '45', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('филе куринное 1кг', '200', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('говядина 1кг', '250', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('грудка куринная 1кг', '225', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('мука пшеничная Весёлый мельник 2кг.', '60', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('макароны Макфа,спагетти', '30', '10','2020-12-30', '360', '2020-12-30'),
            GoodInfo('свинина 1кг', '220', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('голень куринная 1кг', '230', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рис шлифованный 1кг', '40', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('баранина 1кг', '210', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('крылышки куринные 1кг', '180', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('Чай черный Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('Чай зеленый Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('пшено 1кг', '50', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('крупа гречневая 1кг', '60', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('сахар 1кг', '40', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('соль 1 кг', '35', '30','2020-12-30', '720', '2020-12-30')
        ]
            
        for good in sort_amount_list:
            self.database.add(good)

        sort_amount_list = self.database.get_all_goods()

        return sort_amount_list

    def form_sort_price_list(self):
        """
        Function form sort list by price
        :return: return GoodInfoList with
        sort by price
        """
        list_sort_price = DB_Worker()

        list_sort_price_test = [
            GoodInfo('хлеб серый хлебозавод', '30', '0','2020-12-30', '4', '2020-12-30'),
            GoodInfo('яйцо 1 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
            GoodInfo('яйцо 2 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
            GoodInfo('яйцо 3 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
            GoodInfo('макароны Макфа,рожки', '30', '7','2020-12-30', '360', '2020-12-30'),
            GoodInfo('макароны Макфа,спагетти', '30', '10','2020-12-30', '360', '2020-12-30'),
            GoodInfo('булочки плюшки', '30', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('пирожки с картошкой', '30', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('пирожки с картошкой', '30', '2','2020-12-30', '7', '2020-12-30'),
            GoodInfo('пирожки с вишней', '30', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('соль 1 кг', '35', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('сахар 1кг', '40', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('мука пшеничная Весёлый мельник 1кг.', '40', '20','2020-12-30', '720', '2020-12-30'),
            GoodInfo('рис шлифованный 1кг', '40', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('лук репчатый 1кг', '40', '50','2020-12-30', '30', '2020-12-30'),
            GoodInfo('сушки 1кг.', '45', '20','2020-12-30', '7', '2020-12-30'),
            GoodInfo('рис круглозерный 1кг', '45', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('вермишель Макфа 1кг', '45', '2','2020-12-30', '720', '2020-12-30'),
            GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('хлеб ржаной хлебозавод', '50', '20','2020-12-30', '5', '2020-12-30'),
            GoodInfo('пшено 1кг', '50', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('молоко Фермерское', '55', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('пряники 1кг.', '55', '20','2020-12-30', '14', '2020-12-30'),
            GoodInfo('морковь 1кг', '55', '50','2020-12-30', '30', '2020-12-30'),
            GoodInfo('Чай черный Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('Чай зеленый Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('мука пшеничная Весёлый мельник 2кг.', '60', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('крупа гречневая 1кг', '60', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('картофель 1кг', '60', '50','2020-12-30', '30', '2020-12-30'),
            GoodInfo('яблоки Новая Зеландия 1кг', '60', '120','2020-12-30', '21', '2020-12-30'),
            GoodInfo('молоко Простоквашино', '66', '5','2020-12-30', '7', '2020-12-30'),
            GoodInfo('молоко Хорская Буренка', '70', '5','2020-12-30', '3', '2020-12-30'),
            GoodInfo('масло сливочное', '100', '20','2020-12-30', '7', '2020-12-30'),
            GoodInfo('масло подсолнечное', '100', '20','2020-12-30', '7', '2020-12-30'),
            GoodInfo('крылышки куринные 1кг', '180', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('филе куринное 1кг', '200', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('баранина 1кг', '210', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('свинина 1кг', '220', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('грудка куринная 1кг', '225', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('голень куринная 1кг', '230', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('говядина 1кг', '250', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Треска 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Горбуша 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Окунь 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Кета 1кг', '400', '5','2020-12-30', '90', '2020-12-30')
        ]

        for good in list_sort_price_test:
            list_sort_price.add(good)

        return list_sort_price

    def form_sort_name_list(self):
        """
        Function form sort list by name
        :return: return GoodInfoList with
        sort by name
        """
        list_sort_name = DB_Worker()

        list_sort_name_test = [
            GoodInfo('Чай зеленый Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('Чай черный Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('баранина 1кг', '210', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('булочки плюшки', '30', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('вермишель Макфа 1кг', '45', '2','2020-12-30', '720', '2020-12-30'),
            GoodInfo('говядина 1кг', '250', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('голень куринная 1кг', '230', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('грудка куринная 1кг', '225', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('картофель 1кг', '60', '50','2020-12-30', '30', '2020-12-30'),
            GoodInfo('крупа гречневая 1кг', '60', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('крылышки куринные 1кг', '180', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('лук репчатый 1кг', '40', '50','2020-12-30', '30', '2020-12-30'),
            GoodInfo('макароны Макфа,рожки', '30', '7','2020-12-30', '360', '2020-12-30'),
            GoodInfo('макароны Макфа,спагетти', '30', '10','2020-12-30', '360', '2020-12-30'),
            GoodInfo('масло подсолнечное', '100', '20','2020-12-30', '7', '2020-12-30'),
            GoodInfo('масло сливочное', '100', '20','2020-12-30', '7', '2020-12-30'),
            GoodInfo('молоко Простоквашино', '66', '5','2020-12-30', '7', '2020-12-30'),
            GoodInfo('молоко Фермерское', '55', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('молоко Хорская Буренка', '70', '5','2020-12-30', '3', '2020-12-30'),
            GoodInfo('морковь 1кг', '55', '50','2020-12-30', '30', '2020-12-30'),
            GoodInfo('мука пшеничная Весёлый мельник 1кг.', '40', '20','2020-12-30', '720', '2020-12-30'),
            GoodInfo('мука пшеничная Весёлый мельник 2кг.', '60', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('пирожки с вишней', '30', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('пирожки с картошкой', '30', '10','2020-12-30', '7', '2020-12-30'),
            GoodInfo('пирожки с картошкой', '30', '2','2020-12-30', '7', '2020-12-30'),
            GoodInfo('пряники 1кг.', '55', '20','2020-12-30', '14', '2020-12-30'),
            GoodInfo('пшено 1кг', '50', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('рис круглозерный 1кг', '45', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('рис шлифованный 1кг', '40', '10','2020-12-30', '720', '2020-12-30'),
            GoodInfo('рыба мороженая, Горбуша 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Кета 1кг', '400', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Окунь 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('рыба мороженая, Треска 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
            GoodInfo('сахар 1кг', '40', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('свинина 1кг', '220', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('соль 1 кг', '35', '30','2020-12-30', '720', '2020-12-30'),
            GoodInfo('сушки 1кг.', '45', '20','2020-12-30', '7', '2020-12-30'),
            GoodInfo('филе куринное 1кг', '200', '10','2020-12-30', '90', '2020-12-30'),
            GoodInfo('хлеб ржаной хлебозавод', '50', '20','2020-12-30', '5', '2020-12-30'),
            GoodInfo('хлеб серый хлебозавод', '30', '0','2020-12-30', '4', '2020-12-30'),
            GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
            GoodInfo('яблоки Новая Зеландия 1кг', '60', '120','2020-12-30', '21', '2020-12-30'),
            GoodInfo('яйцо 1 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
            GoodInfo('яйцо 2 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
            GoodInfo('яйцо 3 кат.', '30', '40','2020-12-30', '14', '2020-12-30')
        ]

        for good in list_sort_name_test:
            list_sort_name.add(good)
        
        return list_sort_name


    def setUp(self):
        """
        setUp function for set data
        """
        
        with open("config_script.json", "r") as json_data:
            config_data = json.load(json_data)

            logging.basicConfig(
                                filename=config_data["filename_logging"], 
                                filemode=config_data["filemode_logging"],
                                level=config_data["level_logging"], 
                                format=config_data["format_logging"])
        
        

        self.database = DB_Worker()     
        self.info_list = GoodInfoList()
        self.file_goods = FileWork()
        self.file_data = self.file_goods.select_path_file("test")

        if len(self.file_data) > 0:
            self.database.truncate_all_tables()
            self.info_list.get_from_file(self.file_data)

    # def test_sort_amount(self):
    #     """
    #     Function test sort amount
    #     """
    #     sort_amount = self.info_list.sort("amount")
    #     amount_sort_test = self.form_sort_amount_list()

    #     self.assertEqual(sort_amount, amount_sort_test)

    # def test_sort_price(self):
    #     """
    #     Function test sort price
    #     """
    #     sort_price = self.info_list.sort("price")
    #     self.assertEqual(sort_price, self.price_sort_test)
    
    # def test_sort_name(self):
    #     """
    #     Function test sort name
    #     """
    #     sort_name = self.info_list.sort("name")
    #     self.assertEqual(sort_name, self.name_sort_test)

    def test_get_list_ending_goods(self):
        """
        Function test get list with ending goods
        """
        ending_goods_test = self.info_list.get_list_ending_goods()
        self.ending_goods_test = self.form_ending_list_goods()
        
        ending_goods_test = list(ending_goods_test)
        

        self.assertEqual(ending_goods_test, self.ending_goods_test)

    def test_get_list_cheapset_goods(self):
        """
        Function test get list with cheapset goods
        """
        cheapset_goods_test = self.info_list.\
                                    get_list_with_cheap_goods()        
        most_cheapset_test = self.form_cheapset_list_goods()

        cheapset_goods_test = list(cheapset_goods_test)

        self.assertEqual(cheapset_goods_test, 
                         most_cheapset_test)

    def test_get_list_most_expensive(self):
        """
        Function test get list with most expensive goods
        """

        expensive_goods_test = self.info_list.get_list_most_expensive()

        most_expensive_test = self.form_expensive_list_goods()

        self.assertEqual(expensive_goods_test,
                         most_expensive_test)

    def test_product_buy(self):
        """
        Function test product buy
        """
        result_buy = self.info_list.product_buy("соль 1 кг", 5)
        self.database.truncate_all_tables()
        self.assertEqual(result_buy, 175)
    
    def test_product_buy_more_then_have(self):
        """
        Function test product buy more then have
        """
        result_buy = self.info_list.product_buy("соль 1 кг", 50)
        self.assertFalse(result_buy)

    def test_product_buy_with_not_exists_name(self):
        """
        Function test product buy with not exists name
        """
        result_buy = self.info_list.product_buy("Говядина Немецкая 2кг", 3)
        self.assertFalse(result_buy)        

    def test_product_buy_missing_goods(self):
        """
        Function test product buy missings goods
        """
        result_buy = self.info_list.product_buy("хлеб серый хлебозавод", 3)
        self.assertFalse(result_buy)

    def test_add_without_name(self):
        """
        Function test product buy without name
        """
        good = GoodInfo("", "30", "40", "2020-12-30", "14", "2020-12-30")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_not_right_shelf_life(self):
        """
        Function test product buy not right shelf life
        """
        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", "-14", "2020-12-30")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_end_shelf_life(self):
        """
        Function test add with end shelf life
        """
        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-1", "3", "2020-12-1")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_negative_price(self):
        """
        Function test add with negative price
        """
        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", "14", "2020-12-30")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)
    
    def test_add_with_negative_amount(self):
        """
        Function test add with negative amount
        """
        good = GoodInfo("яйцо 1 кат.", "30", "-40", "2020-12-30", "14", "2020-12-30")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)

    def test_remove(self):
        """
        Function test remove of GoodInfoList
        """
        test_remove = self.info_list.remove("сахар 1кг")
        self.assertEqual(test_remove, "сахар 1кг")

    def test_remove_expensive(self):
        """
        Function test remove expensive of GoodInfoList
        """
        test_remove_expensive = self.info_list.remove_expensive()
        self.assertTrue(test_remove_expensive)
    
    def test_get_std(self):
        """
        Function test standart deviation
        """

        std = self.info_list.get_std()
        self.assertEqual(std, 111.08728376994648) 
    
    def test_amount_value(self):
        """
        Function test amount value
        """
        dict_with_value = self.info_list.get_value_info()
        self.assertEqual(dict_with_value['amount'], 26)

    def test_mean_value(self):
        """
        Function test mean value
        """
        dict_with_value = self.info_list.get_value_info()
        print(dict_with_value["amount"])
        self.assertEqual(dict_with_value['mean'], 135.0)


if __name__ == "main":
    unittest.main()
