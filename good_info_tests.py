from good_info import GoodInfoList
from good_info import GoodInfo
import unittest
from file_work import FileWork

info_list = GoodInfoList()
file_goods = FileWork()
file_data = file_goods.select_path_file()
file_goods.save_in_directory()
    
if len(file_data) > 0:
    info_list.get_from_file(file_data)


class GoodInfoListTest(unittest.TestCase):

    def test_get_std(self):
        std = info_list.get_std()
        self.assertEqual(std, 93.95660364253186) 
    
    def test_info_list_len(self):
        test_info_list = len(info_list)
        self.assertEqual(test_info_list, 47)

    def test_amount_value(self):
        dict_with_value = info_list.get_value_info()
        self.assertEqual(dict_with_value['amount'], 903)

    def test_mean_value(self):
        dict_with_value = info_list.get_value_info()
        self.assertEqual(dict_with_value['mean'], 96.82978723404256)

    def test_get_from_file(self):
        info_list_test = GoodInfoList()
        test_get_from_file = info_list_test.get_from_file(file_data)
        self.assertTrue(test_get_from_file)

    def test_get_from_file_with_empty_string(self):
        info_list_test = GoodInfoList()
        test_get_from_file = info_list_test.get_from_file(file_data)
        self.assertTrue(test_get_from_file)
    
    def test_get_from_file_with_not_valid_string(self):
        info_list_test = GoodInfoList()
        test_get_from_file = info_list_test.get_from_file(file_data)
        self.assertTrue(test_get_from_file)        

    def test_sort_amount(self):
        sort_amount = info_list.sort("amount")
        self.assertEqual(sort_amount, info_list.sort("amount"))

    def test_sort_price(self):
        sort_amount = info_list.sort("price")
        self.assertEqual(sort_amount, info_list.sort("price"))
    
    def test_sort_name(self):
        sort_amount = info_list.sort("name")
        self.assertEqual(sort_amount, info_list.sort("name"))

    def test_product_buy(self):
        result_buy = info_list.product_buy("соль 1 кг", 5)
        self.assertEqual(result_buy, 175)
    
    def test_product_buy_more_then_have(self):
        result_buy = info_list.product_buy("соль 1 кг", 50)
        self.assertFalse(result_buy)

    def test_product_buy_with_not_exists_name(self):
        result_buy = info_list.product_buy("Говядина Немецкая 2кг", 3)
        self.assertFalse(result_buy)        

    def test_product_buy_missing_goods(self):
        result_buy = info_list.product_buy("хлеб серый хлебозавод", 3)
        self.assertFalse(result_buy)

    def test_get_list_ending_goods(self):
        ending_goods_test = info_list.get_list_ending_goods()
        self.assertEqual(ending_goods_test, info_list.get_list_ending_goods())

    def test_get_list_most_expensive(self):
        expensive_goods_test = info_list.get_list_most_expensive()
        self.assertEqual(expensive_goods_test, info_list.get_list_most_expensive())

    def test_add_without_name(self):

        good = GoodInfo("", "30", "40", "2020-12-30", "14", "2020-12-30")
        check_product_data = info_list.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_not_right_shell_life(self):

        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", "-14", "2020-12-30")
        check_product_data = info_list.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_end_shell_life(self):

        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-1", "3", "2020-12-1")
        check_product_data = info_list.add(good)

        self.assertFalse(check_product_data)

    def test_add_with_negative_price(self):

        good = GoodInfo("яйцо 1 кат.", "-30", "40", "2020-12-30", "14", "2020-12-30")
        check_product_data = info_list.add(good)

        self.assertFalse(check_product_data)
    
    def test_add_with_negative_amount(self):

        good = GoodInfo("яйцо 1 кат.", "30", "-40", "2020-12-30", "14", "2020-12-30")
        check_product_data = info_list.add(good)

        self.assertFalse(check_product_data)

    def test_remove(self):
        test_remove = info_list.remove("сахар 1кг")
        self.assertTrue(test_remove)

    def test_remove_expensive(self):
        test_remove_expensive = info_list.remove_expensive()
        self.assertEqual(test_remove_expensive, "рыба мороженая, Кета 1кг")
    

if __name__ == "main":
    unittest.main()
