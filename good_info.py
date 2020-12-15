from math import sqrt

class GoodInfo:
    """
    Represents good info

    Attributes:

    name (str): name product
    price (float): price product
    amount (int): amount product

    Methods:

    __init__(str, float, int)
    __str__()

    """

    def __init__(self, name, price, amount):
        """
        Initialize name, price, amount

        :param name: name product
        :type name: string

        :param price: price product
        :type price: Number

        :param amount: amount product
        :type amount: Number

        """
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        """
        Function make string with represents good
        :return: string represents good
        :rtype: string
        """
        return "{name} : (Количество) {amount} (Цена) {price}".format(
                name=self.name,
                amount=self.amount,
                price=self.price
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
    __getitem__(key)
    get_value_info()
    get_list_with_cheap_goods()

    """

    def __init__(self):
        """ 
        Initiliaize empty list with no goods
        """
        self.list_with_goods = list()

    def __len__(self):
        """
        Return len GoodInfoList
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
        print(value_info)
        squared_deviations = list()
        
        for good_data in self.list_with_goods:
            squared_deviations.append((good_data.price - mean) ** 2)
        
        dispersion = sum(squared_deviations) / len(self.list_with_goods)

        return sqrt(dispersion)
        
    def add(self, name, price, amount):
        """"
        :param name: Name Good
        :param price: Price good
        :param amount: amount good
        :type name: string
        :type price: Number
        :type amount: Number
        :return: function nothing return
        """
        self.list_with_goods.append(GoodInfo(name, price, amount))

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
                self.add(name_product, price_product, product_amount)
            else:
                print("Следующая строка не была обработана: ", product)

    @staticmethod
    def __check_product_data(good_data):
        """
        Check format data product from list with products
        :param good_data: list with data about product
        :type good_data: list
        :return: Return True if format right else return
        false if format not right
        :rtype: Return bool value
        """

        if len(good_data) != 3:
            return False

        if  (len(good_data[0]) == 0 and 
            len(good_data[1]) == 0 and len(good_data[2]) == 0):
            return False
        
        good_data[2] = good_data[2].replace('\n', '')

        if good_data[1].isdigit() and good_data[2].isdigit():
            return True
        else:
            return False
       
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

    def __getitem__(self, key):
        """
        receiving  by []
        :param key: index in list with goods
        :type key: Number
        :return: object by key
        :rtype: object good from list with goods if exsits good by
        key, else raise IndexError
        """
        if self.list_with_goods[key] in self.list_with_goods:
            return self.list_with_goods[key]
        else:
            raise IndexError
    
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
