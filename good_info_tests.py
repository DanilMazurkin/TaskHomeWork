import json
import logging
import good_info
from good_info import GoodInfoList
from good_info import GoodInfo
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
            GoodInfo('макароны Макфа,рожки', '30', '7','2020-12-30', '360', '2020-12-30'),
            GoodInfo('макароны Макфа,спагетти', '30', '10','2020-12-30', '360', '2020-12-30')
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
        ]

        for good in list_with_objects_ending_test:
            self.database.add(good)

        list_with_ending_goods = self.database.get_all_goods()

        return list_with_ending_goods

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
            self.info_list.get_from_file(self.file_data)

    def tearDown(self):
        """
        Execute after execute test
        """
        self.database.truncate_all_tables()

    def test_get_list_ending_goods(self):
        """
        Function test get list with ending goods
        """
        ending_goods_test = self.info_list.get_list_ending_goods()
        ending_goods_test_list = self.form_ending_list_goods()        

        self.assertEqual(ending_goods_test, ending_goods_test_list)

    def test_get_list_cheapset_goods(self):
        """
        Function test get list with cheapset goods
        """
        cheapset_goods_test = self.info_list.\
                                    get_list_with_cheap_goods()        
        most_cheapset_test = self.form_cheapset_list_goods()

        self.assertEqual(cheapset_goods_test, most_cheapset_test)

    def test_get_list_most_expensive(self):
        """
        Function test get list with most expensive goods
        """

        expensive_goods_test = self.info_list.get_list_most_expensive()
        most_expensive_test = self.form_expensive_list_goods()

        self.assertEqual(expensive_goods_test, most_expensive_test)

    def test_product_buy(self):
        """
        Function test product buy
        """
        result_buy = self.info_list.product_buy("соль 1 кг", 5)
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
        good = GoodInfo("", "30", "40", "2020-12-30", 
                        "14", "2020-12-30")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_not_right_shelf_life(self):
        """
        Function test product buy not right shelf life
        """
        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", 
                        "-14", "2020-12-30")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_end_shelf_life(self):
        """
        Function test add with end shelf life
        """
        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-1", 
                        "3", "2020-12-1")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_negative_price(self):
        """
        Function test add with negative price
        """
        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", 
                        "14", "2020-12-30")
        check_product_data = self.database.add(good)

        self.assertFalse(check_product_data)
    
    def test_add_with_negative_amount(self):
        """
        Function test add with negative amount
        """
        good = GoodInfo("яйцо 1 кат.", "30", "-40", "2020-12-30", 
                        "14", "2020-12-30")
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
