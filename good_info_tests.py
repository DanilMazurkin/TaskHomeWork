from good_info import GoodInfoList
from good_info import GoodInfo
import unittest
from file_work import FileWork


class GoodInfoListTest(unittest.TestCase):

    def setUp(self):
        self.info_list = GoodInfoList()
        self.file_goods = FileWork()
        self.file_data = self.file_goods.select_path_file("test")

        if len(self.file_data) > 0:
            self.info_list.get_from_file(self.file_data)
            self.most_expensive_test = GoodInfoList()
            self.most_expensive_test.add(
                                    GoodInfo("рыба мороженая, Кета 1кг", 
                                    "400", "5", "2020-12-30", "90", "2020-12-30"))
            
            self.most_cheapset_test = GoodInfoList()
            
            list_with_object_cheapset_test = [
                GoodInfo('хлеб серый хлебозавод', '30', '0','2020-12-30', '4', '2020-12-30'),
                GoodInfo('яйцо 1 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
                GoodInfo('яйцо 2 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
                GoodInfo('яйцо 3 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
                GoodInfo('макароны Макфа,рожки', '30', '7','2020-12-30', '360', '2020-12-30'),
                GoodInfo('макароны Макфа,спагетти', '30', '10','2020-12-30', '360', '2020-12-30'),
                GoodInfo('булочки плюшки', '30', '10','2020-12-30', '7', '2020-12-30'),
                GoodInfo('пирожки с картошкой', '30', '10','2020-12-30', '7', '2020-12-30'),
                GoodInfo('пирожки с картошкой', '30', '2','2020-12-30', '7', '2020-12-30'),
                GoodInfo('пирожки с вишней', '30', '10','2020-12-30', '7', '2020-12-30')  
            ]

            for good in list_with_object_cheapset_test:
                self.most_cheapset_test.add(good)
            
            self.list_with_object_ending_test = GoodInfoList()

            list_with_objects_ending_test = [
                GoodInfo('хлеб серый хлебозавод', '30', '0','2020-12-30', '4', '2020-12-30'),
                GoodInfo('пирожки с картошкой', '30', '2','2020-12-30', '7', '2020-12-30'),
                GoodInfo('вермишель Макфа 1кг', '45', '2','2020-12-30', '720', '2020-12-30')
            ]

            for good in list_with_objects_ending_test:
                self.list_with_object_ending_test.add(good)

            self.list_sort_amount = GoodInfoList()

            list_sort_amount = [
                GoodInfo('хлеб серый хлебозавод', '30', '0','2020-12-30', '4', '2020-12-30'),
                GoodInfo('пирожки с картошкой', '30', '2','2020-12-30', '7', '2020-12-30'),
                GoodInfo('вермишель Макфа 1кг', '45', '2','2020-12-30', '720', '2020-12-30'),
                GoodInfo('молоко Хорская Буренка', '70', '5','2020-12-30', '3', '2020-12-30'),
                GoodInfo('молоко Простоквашино', '66', '5','2020-12-30', '7', '2020-12-30'),
                GoodInfo('рыба мороженая, Кета 1кг', '400', '5','2020-12-30', '90', '2020-12-30'),
                GoodInfo('рыба мороженая, Треска 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
                GoodInfo('рыба мороженая, Горбуша 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
                GoodInfo('рыба мороженая, Окунь 1кг', '300', '5','2020-12-30', '90', '2020-12-30'),
                GoodInfo('макароны Макфа,рожки', '30', '7','2020-12-30', '360', '2020-12-30'),
                GoodInfo('молоко Фермерское', '55', '10','2020-12-30', '7', '2020-12-30'),
                GoodInfo('макароны Макфа,спагетти', '30', '10','2020-12-30', '360', '2020-12-30'),
                GoodInfo('говядина 1кг', '250', '10','2020-12-30', '90', '2020-12-30'),
                GoodInfo('свинина 1кг', '220', '10','2020-12-30', '90', '2020-12-30'),
                GoodInfo('баранина 1кг', '210', '10','2020-12-30', '90', '2020-12-30'),
                GoodInfo('филе куринное 1кг', '200', '10','2020-12-30', '90', '2020-12-30'),
                GoodInfo('грудка куринная 1кг', '225', '10','2020-12-30', '90', '2020-12-30'),
                GoodInfo('голень куринная 1кг', '230', '10','2020-12-30', '90', '2020-12-30'),
                GoodInfo('крылышки куринные 1кг', '180', '10','2020-12-30', '90', '2020-12-30'),
                GoodInfo('мука пшеничная Весёлый мельник 2кг.', '60', '10','2020-12-30', '720', '2020-12-30'),
                GoodInfo('булочки плюшки', '30', '10','2020-12-30', '7', '2020-12-30'),
                GoodInfo('пирожки с картошкой', '30', '10','2020-12-30', '7', '2020-12-30'),
                GoodInfo('пирожки с вишней', '30', '10','2020-12-30', '7', '2020-12-30'),
                GoodInfo('рис шлифованный 1кг', '40', '10','2020-12-30', '720', '2020-12-30'),
                GoodInfo('рис круглозерный 1кг', '45', '10','2020-12-30', '720', '2020-12-30'),
                GoodInfo('масло сливочное', '100', '20','2020-12-30', '7', '2020-12-30'),
                GoodInfo('масло подсолнечное', '100', '20','2020-12-30', '7', '2020-12-30'),
                GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
                GoodInfo('Чай черный Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
                GoodInfo('чай черный Greenfield 10 пак.', '50', '20','2020-12-30', '1080', '2020-12-30'),
                GoodInfo('Чай зеленый Lipton 10 пак.', '60', '20','2020-12-30', '1080', '2020-12-30'),
                GoodInfo('мука пшеничная Весёлый мельник 1кг.', '40', '20','2020-12-30', '720', '2020-12-30'),
                GoodInfo('хлеб ржаной хлебозавод', '50', '20','2020-12-30', '5', '2020-12-30'),
                GoodInfo('сушки 1кг.', '45', '20','2020-12-30', '7', '2020-12-30'),
                GoodInfo('пряники 1кг.', '55', '20','2020-12-30', '14', '2020-12-30'),
                GoodInfo('сахар 1кг', '40', '30','2020-12-30', '720', '2020-12-30'),
                GoodInfo('соль 1 кг', '35', '30','2020-12-30', '720', '2020-12-30'),
                GoodInfo('пшено 1кг', '50', '30','2020-12-30', '720', '2020-12-30'),
                GoodInfo('крупа гречневая 1кг', '60', '30','2020-12-30', '720', '2020-12-30'),
                GoodInfo('яйцо 1 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
                GoodInfo('яйцо 2 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
                GoodInfo('яйцо 3 кат.', '30', '40','2020-12-30', '14', '2020-12-30'),
                GoodInfo('картофель 1кг', '60', '50','2020-12-30', '30', '2020-12-30'),
                GoodInfo('лук репчатый 1кг', '40', '50','2020-12-30', '30', '2020-12-30'),
                GoodInfo('морковь 1кг', '55', '50','2020-12-30', '30', '2020-12-30'),
                GoodInfo('яблоки Новая Зеландия 1кг', '60', '120','2020-12-30', '21', '2020-12-30')
            ]
            
            for good in list_sort_amount:
                self.list_sort_amount.add(good)
            
            self.list_sort_price = GoodInfoList()

            list_sort_price = [
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

            for good in list_sort_price:
                self.list_sort_price.add(good)

            self.list_sort_name = GoodInfoList()

            list_sort_name = [
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

            for good in list_sort_name:
                self.list_sort_name.add(good)

    def test_get_std(self):
        std = self.info_list.get_std()
        self.assertEqual(std, 94.65772586621006) 
    
    def test_info_list_len(self):
        test_info_list = len(self.info_list)
        self.assertEqual(test_info_list, 46)

    def test_amount_value(self):
        dict_with_value = self.info_list.get_value_info()
        self.assertEqual(dict_with_value['amount'], 901)

    def test_mean_value(self):
        dict_with_value = self.info_list.get_value_info()
        self.assertEqual(dict_with_value['mean'], 97.95652173913044)

    def test_get_from_file(self):
        test_get_from_file = self.info_list.get_from_file(self.file_data)
        self.assertTrue(test_get_from_file)

    def test_get_from_file_with_empty_string(self):
        test_get_from_file = self.info_list.get_from_file(self.file_data)
        self.assertTrue(test_get_from_file)
    
    def test_get_from_file_with_not_valid_string(self):
        test_get_from_file = self.info_list.get_from_file(self.file_data)
        self.assertTrue(test_get_from_file)        

    def test_sort_amount(self):
        sort_amount = self.info_list.sort("amount")
        self.assertTrue(sort_amount == self.list_sort_amount)

    def test_sort_price(self):
        sort_price = self.info_list.sort("price")
        self.assertTrue(sort_price, self.list_sort_price)
    
    def test_sort_name(self):
        sort_name = self.info_list.sort("name")
        self.assertEqual(sort_name, self.list_sort_name)

    def test_get_list_ending_goods(self):
        ending_goods_test = self.info_list.get_list_ending_goods()
        self.assertTrue(ending_goods_test == self.list_with_object_ending_test)

    def test_get_list_cheapset_goods(self):
        cheapset_goods_test = self.info_list.get_list_with_cheap_goods()
        self.assertTrue(cheapset_goods_test == self.most_cheapset_test)

    def test_get_list_most_expensive(self):
        expensive_goods_test = self.info_list.get_list_most_expensive()

        self.assertTrue(expensive_goods_test == self.most_expensive_test)

    def test_product_buy(self):
        result_buy = self.info_list.product_buy("соль 1 кг", 5)
        self.assertEqual(result_buy, 175)
    
    def test_product_buy_more_then_have(self):
        result_buy = self.info_list.product_buy("соль 1 кг", 50)
        self.assertFalse(result_buy)

    def test_product_buy_with_not_exists_name(self):
        result_buy = self.info_list.product_buy("Говядина Немецкая 2кг", 3)
        self.assertFalse(result_buy)        

    def test_product_buy_missing_goods(self):
        result_buy = self.info_list.product_buy("хлеб серый хлебозавод", 3)
        self.assertFalse(result_buy)

    def test_add_without_name(self):

        good = GoodInfo("", "30", "40", "2020-12-30", "14", "2020-12-30")
        check_product_data = self.info_list.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_not_right_shell_life(self):

        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", "-14", "2020-12-30")
        check_product_data = self.info_list.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_end_shell_life(self):

        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-1", "3", "2020-12-1")
        check_product_data = self.info_list.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_negative_price(self):

        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", "14", "2020-12-30")
        check_product_data = self.info_list.add(good)

        self.assertFalse(check_product_data)
    
    def test_add_with_negative_amount(self):

        good = GoodInfo("яйцо 1 кат.", "30", "-40", "2020-12-30", "14", "2020-12-30")
        check_product_data = self.info_list.add(good)

        self.assertFalse(check_product_data)

    def test_remove(self):
        test_remove = self.info_list.remove("сахар 1кг")
        self.assertTrue(test_remove)

    def test_remove_expensive(self):
        test_remove_expensive = self.info_list.remove_expensive()
        self.assertEqual(test_remove_expensive, "рыба мороженая, Кета 1кг")
    

if __name__ == "main":
    unittest.main()