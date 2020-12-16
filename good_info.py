from math import sqrt
from datetime import datetime, timedelta

class GoodInfo:
    """
    Represents good info

    Attributes:

    name (str): name product
    price (float): price product
    amount (int): amount product
    date_import (datetime): date import
    shelf_life (int) (shelf_life): shelf life

    Methods:

    __init__(str, float, int)
    __str__()

    """

    def __init__(self, name, price, amount, date_import, shelf_life):
        """
        Initialize name, price, amount, date_import, shellf_life

        :param name: name product
        :type name: string
        :param price: price product
        :type price: Number
        :param amount: amount product
        :type amount: Number
        :param date_import: string with date
        :type date_import: string
        :param shell_life: Shell life good
        :type shell_life: Integer
        """
        self.name = name
        self.price = price
        self.amount = amount
        self.date_import = date_import
        self.shelf_life = shelf_life

    def __str__(self):
        """
        Function make string with represents good
        :return: string represents good
        :rtype: string
        """
        return "{name} : (Количество) {amount} (Цена) {price} \n \
                (Дата) {date} (Срок годности) {shelf_life} \n".format(
                name=self.name,
                amount=self.amount,
                price=self.price,
                date=self.date_import,
                shelf_life=self.shelf_life
        )        


class GoodInfoList:
    """
    Represents good info

    Attributes:

    list_with_goods (list(GoodInfo)): list of goods

    Methods:

    __init__(str, float, int)
    __str__()
    add(name, price, amount)
    get_from_file(filename)
    add_goods_in_list(list_with_products)
    __check_product_data(good_data)
    remove(name)
    remove_expensive()
    get_list_most_expensive()
    get_list_ending_goods()
    sort(key)
    __getitem__(name)
    get_value_info()
    get_list_with_cheap_goods()

    """

    def __init__(self):
        """ 
        Initiliaize empty list with no goods
        """
        self.list_with_goods = list()

    def __str__(self):
        """
        Function make string with represents GoodInfo
        :return: string represents GoodInfo
        :rtype: string
        """
        string_with_list = ""

        for elem in self.list_with_goods:
            string_with_list += str(elem) + '\n'
       
        return string_with_list

    def __len__(self):
        """
        Return length GoodInfoList
        """
        return len(self.list_with_goods)

    def remove_last(self):
        """
        Function remove last good in ListGoods
        :return: Nothing return
        """
        index_last_good = len(self.list_with_goods) - 1
        last_good = self.list_with_goods[index_last_good]

        self.remove(last_good.name)

    def get_std(self):
        """
        Function calculate standard deviation
        :return: standard deviation
        :rtype: float
        """
        value_info = self.get_value_info()
        mean = value_info['mean']
        squared_deviations = list()
        
        for good_data in self.list_with_goods:
            squared_deviations.append((good_data.price - mean) ** 2)
        
        dispersion = sum(squared_deviations) / len(self.list_with_goods)

        return sqrt(dispersion)
        
    def add(self, name, price, amount, date_import, shelf_life):
        """"
        :param name: Name Good
        :param price: Price good
        :param amount: amount good
        :type name: string
        :type price: Number
        :type amount: Number
        :return: function nothing return
        """
        self.list_with_goods.append(GoodInfo(name, price, amount, 
                                            date_import, shelf_life))

    @staticmethod
    def get_from_file(filename):
        """
        Forms list of goods from file data
        :param filename: filepath for data
        :type filename: string
        :return: Return list with goods
        :rtype: list 
        """
        file_data = open(filename, "r", encoding="utf-8")
        list_from_file = file_data.readlines()        
        file_data.close()
        
        return list_from_file

    def add_goods_in_list(self, list_with_products):
        """
        Add good in list
        :param list_with_products: list of GoodInfo
        :type list_with_products: list
        :return: Function nothing return
        """
        for product in list_with_products:
            product_data = product.split(":")

            if self.__check_product_data(product_data):
                name_product = product_data[0]
                price_product = int(product_data[1])
                product_amount = int(product_data[2])
                product_date =  datetime.strptime(product_data[3], "%Y-%m-%d")
                shelf_life = int(product_data[4])
                self.add(name_product, price_product, product_amount, 
                        product_date, shelf_life)
            else:
                print("Следующая строка не была обработана: ", product)

    def __check_product_data(self, good_data):
        """
        Check format data product from list with products
        :param good_data: list with data about product
        :type good_data: list
        :return: Return True if format right else return
        false if format not right
        :rtype: Return bool value
        """

        if len(good_data) != 5:
            return False

        if  (len(good_data[0]) == 0 and 
            len(good_data[1]) == 0 and len(good_data[2]) == 0):
            return False
        
        good_data[2] = good_data[2].replace('\n', '')

        if (good_data[1].isdigit() and good_data[2].isdigit() 
            and self.__check_date(good_data[3])):
            return True
        else:
            return False
    
    @staticmethod
    def __check_shell_life_good(good_date, shelf_life):
        """
        Check shell life
        :param good_date: str with date
        :type good_date: string
        :param shelf_life: shelf life of date
        :type shelf_life:
        :return: return true if shelf life end and return
        False if shelf life not end
        """
        
        shelf_life = timedelta(days=int(shelf_life))
        ending_shelf_life = good_date + shelf_life
        today = datetime.today()

        if today > ending_shelf_life:
            return True
        else:
            return False

    @staticmethod
    def __check_date(good_date):
        """
        Check date on right format
        :param good_date: string with date 
        :type good_date: string
        :return: true if date of delivery less then 
        current date, else false
        :rtype: bool 
        """
        date_import =  datetime.strptime(good_date, "%Y-%m-%d")
        today = datetime.today()

        if date_import < today:
            print("Дата поставки меньше текущей!")
            return False
        else:
            return True
    
    def check_date_import(self):
        """
        If the expiration in list date has expired, then the product is removed
        :return: GoodInfoList with removing goods
        :rtype: GoodInfoList
        """

        list_of_removing_goods = GoodInfoList()

        for good in self.list_with_goods:
            if self.__check_shell_life_good(good.date_import, good.shelf_life):
                list_of_removing_goods.add(good.name, good.price, good.amount, 
                                           good.date_import, good.shelf_life)
                self.remove(good.name)
    
        return list_of_removing_goods
        
    def remove(self, name):
        """
        Remove object with name
        :param name: name good
        :type name: string
        """
        for good in self.list_with_goods:
            if good.name == name:
                print("Удаленный товар: ", good.name)
                self.list_with_goods.remove(good)

    def remove_expensive(self):
        """
        Remove object with maximum price
        """
        most_expensive = self.get_list_most_expensive()
        max_price = most_expensive[0].price

        for good in self.list_with_goods:
            if good.price == max_price:
                print("Удаленный товар с самой большой ценой: ", good)
                self.list_with_goods.remove(good)

    def get_list_most_expensive(self):
        """
        Get list with most expensive goods
        :return: list with most expensive goods
        :rtype: list
        """
        most_expensive_goods = list()
        max_price = 0

        for good in self.list_with_goods:
            if good.price > max_price:
                max_price = good.price

        for good in self.list_with_goods:
            if good.price == max_price:
                most_expensive_goods.append(good)

        return most_expensive_goods

    def get_list_with_cheap_goods(self):
        """
        Get list with most cheapset goods
        :return: list with most cheapset goods
        :rtype: list
        """

        most_cheapset = list()
        min_price = 9999

        for good in self.list_with_goods:
            if good.price < min_price:
                min_price = good.price
        
        for good in self.list_with_goods:
            if good.price == min_price:
                most_cheapset.append(good)
        
        return most_cheapset

    def get_list_ending_goods(self):
        """
        Get list with ending goods
        :return: list with enging goods
        :rtype: list
        """
        ending_goods = list()

        for good in self.list_with_goods:
            if good.amount < 5:
                ending_goods.append(good)
        
        return ending_goods

    def sort(self, key):
        """
        Sort list with goods by key
        :param key: name field by which need sort
        :type key: string
        :return: sorted list with goods
        :rtype: list
        """

        if key == "price":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.price)
            return sort_list
        elif key == "amount":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.amount)
            return sort_list
        elif key == "name":
            sort_list = sorted(
                                self.list_with_goods,
                                key=lambda good: good.name)
            return sort_list
        else:
            raise AttributeError

    def __getitem__(self, name):
        """
        receiving  by []
        :param key: name in list with goods
        :type key: string
        :return: object by key
        :rtype: object good from list with goods if exsits good by
        key, else raise KeyError
        """
        
        list_of_goods = GoodInfoList()

        for good in self.list_with_goods:
            if good.name == name:
                list_of_goods.add(good.name, good.price, good.amount, 
                                  good.date_import, good.shelf_life)
        
        if len(list_of_goods) == 0:
            raise KeyError
        else:
            return list_of_goods

    def get_value_info(self): 
        """ 
        Function get values about products
        :return: Function return dictionary with 
        amount products and mean value
        if list_with_goods is empty function return -1
        :rtype: Return dictionary with key:amount and key:mean and
        :amount=(Number)
        :mean=(float Number)
        """
        if len(self.list_with_goods) == 0:
            return -1

        total_price = 0
        amount_product = 0

        for good in self.list_with_goods:
            total_price += good.price
            amount_product += good.amount
            
        mean = total_price / amount_product
        
        return {'amount': amount_product, 'mean': mean}
