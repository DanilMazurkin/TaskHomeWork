from good_info import GoodInfo
from math import sqrt
import logging 
from db_worker import DB_Worker
from db_models import Good, Provider, Delivery, Shelf
from sqlalchemy import func, text, update


class GoodInfoListDB:
    """
    Represents good info list in database

    Attributes:
    database (Database): Database object
    session (Session): Session object
    
    Methods:
    __init__()
    remove_expensive()
    remove_last()
    get_std()
    remove()
    get_list_ending_goods()
    get_list_most_expensive()
    get_list_with_cheap_goods()
    sort(name)
    get_value_info()
    product_buy(name, amount)
    add(good_info)
    get_from_file()
    add_record_shelf(shelf_life)
    add_record_delivery(date_delivery)
    add_record_provider(name)
    add_record_good(name, amount, price, 
                    id_provider, id_date, id_shelf)
    get_id_provider_by_name(name)
    get_id_delivery_by_date(date_delivery):
    get_id_shelf(shelf_life)

    """

    def __init__(self):
        """
        Initialize database and session,
        and also set tables 
        """
        self.database = DB_Worker()
        self.session = self.database.get_session() 
        self.database.set_tables()

    def remove_expensive(self):
        """
        Remove most expensive good from 
        table goods in database
        """
        max_price_db = self.session.query(func.max(Good.price)).scalar()

        self.session.query(Good).filter(Good.price == max_price_db).\
                    delete(synchronize_session='evaluate')
        self.session.commit()
    
    def remove_last(self):
        """
        Remove last good from goods
        from table goods in database
        """
        count_goods = self.session.query(func.count(Good.id)).scalar()
        
        self.session.query(Good).filter(Good.id == count_goods).\
                    delete(synchronize_session='evaluate')            
        self.session.commit()
    
    def get_std(self):
        """
        Calculate standart deviation
        by price
        :return: standart deviation
        :rtype: Number 
        """

        price_goods = self.session.query(Good.price)
        
        n = self.session.query(func.count(Good.id)).scalar()

        values = self.get_value_info()
        mean = values['mean']

        deviations = [(good.price - mean) ** 2 for good in price_goods]
        variance = sum(deviations) / n
        
        return sqrt(variance)

    def remove(self, name):
        """
        Remove good by name
        """
        
        self.session.query(Good).filter(Good.name == name).\
                delete(synchronize_session='evaluate')
        self.session.commit()

    def get_list_ending_goods(self):
        """
        Get list where amount less five
        :return: goods from database
        :rtype: list Query 
        """
        goods = self.session.query(Good).filter(Good.amount < 5)

        return goods
    
    def get_list_most_expensive(self):
        """
        Get list with most 
        expensive goods
        :return: Query list with goods expensive
        :rtype: Query list
        """
        max_price_db = self.session.query(func.max(Good.price)).scalar()

        goods_expensive = self.session.query(Good).filter(
                                                Good.price == max_price_db)

        return goods_expensive

    def get_list_with_cheap_goods(self):
        """
        Get list with cheap goods
        :return: Query list with cheap goods
        :rtype: Query list
        """

        min_price_db = self.session.query(func.min(Good.price)).scalar()

        cheaps_goods = self.session.query(Good).filter(
                                                Good.price == min_price_db)

        return cheaps_goods
    
    def sort(self, name):
        """
        Sort list with goods by key
        :param key: name field by which need sort
        :type key: string
        :return: sorted list with goods
        :rtype: Query list
        """

        if name == "price":
            order_by_price = self.session.query(Good).\
                                            order_by(Good.price)            
            return order_by_price
        
        elif name == "amount":
            order_by_amount = self.session.query(Good).\
                                            order_by(Good.amount)

            return order_by_amount

        elif name == "name":
            order_by_name = self.session.query(Good).\
                                        order_by(Good.name)
            return order_by_name

        else:
            raise AttributeError
    
    def get_value_info(self):
        """ 
        Function get values about products
        :return: Function return dictionary with 
        amount products and mean value
        if column good price is empty 
        function return -1
        :rtype: Return dictionary with key:amount and key:mean and
        :amount=(Number)
        :mean=(float Number)
        """
        
        count = self.session.query(func.count(Good.id)).scalar()
        
        if count == 0:
            return -1

        mean = self.session.query(func.avg(Good.price)).scalar()

        return {'amount': count, 'mean': mean}        

    def product_buy(self, name, amount):
        """
        Function allows you to buy a product
        :param name: name good
        :type name: string
        :param amount: amount goods
        :type amount: integer
        :return: Function return False if total amount goods less
        then amount, function return false if goood end, function
        return earnings else
        :rtype: bool if false, else integer
        """

        count_product_by_name = self.session.query(Good).\
                                                filter(name == Good.name).\
                                                count()
        if count_product_by_name == 0:
            logging.info("Нет товара с именем {name}".format(name=name))
            print("Нет товара с именем {name}".format(name=name))
            return False

        goods_find_list = self.session.query(Good).\
                                            filter(name == Good.name)
        goods_find_list_count = self.session.query(Good).\
                                            filter(name == Good.name).\
                                            count()
        
        availability = any(good.amount > 0 for good in goods_find_list)

        if availability is False:
            logging.info("Товар закончился ({product}) "
                        "(выручка - None)".format(product=name))
            print("Товар закончился ({product}) "
                        "(выручка - None)".format(product=name))
            return False
        
        total_amount = sum([good.amount for good in goods_find_list])

        if goods_find_list_count == 1 and total_amount < amount:
            logging.info("Количество запрашиваемых товаров больше "
                        "чем имеется в наличии (выручка - None)")
            print("Количество запрашиваемых товаров больше "
                        "чем имеется в наличии (выручка - None)")
            return False
        
        if goods_find_list_count > 1:
            
            min_date = min([good.dates_delivery.date_manufacture 
                            for good in goods_find_list
                            if good.amount > amount
                            ])
            earnings = 0

            for good in goods_find_list:
                if good.date_manufacture == min_date:
                    good.amount -= amount
                    earnings = amount * good.price
                    self.session.query(Good).\
                        filter(Good.name == name).\
                        update({"amount": (Good.amount - amount)})
                    self.session.commit()

            return earnings
        
        elif goods_find_list_count == 1:
            good = goods_find_list[0]
            earnings = amount * good.price

            self.session.query(Good).\
                        filter(Good.name == name).\
                        update({"amount": (Good.amount - amount)})
            self.session.commit()

            return earnings

    def add(self, good_info):
        """"
        Add GoodInfo in Database table goods
        :param good_info: object GoodInfo
        :type good_info: GoodInfo
        :return: function nothing return
        """

        if (GoodInfo.check_product_data(good_info.name, 
                                       good_info.price, 
                                       good_info.amount, 
                                       good_info.date_import, 
                                       good_info.shelf_life) and
            
            GoodInfo.check_shell_life_good(good_info.date_manufacture, 
                                           good_info.shelf_life)):


            self.add_record_shelf(good_info.shelf_life)
            self.add_record_delivery(good_info.date_import)
            self.add_record_provider("Default")
            
            id_shelf = self.get_id_shelf(good_info.shelf_life)
            id_provider = self.get_id_provider_by_name("Default")
            
            id_date_delivery = self.get_id_delivery_by_date(
                                                    good_info.date_import)
            

            self.add_record_good(good_info.name,
                                     good_info.amount,
                                     good_info.price,
                                     id_provider, 
                                     id_shelf)
            
            return True
        else:
            logging.error("Следующая строка не была обработана: {good_info}".format(
                                                                   good_info=good_info))
            return False
    
    def get_from_file(self, list_from_file):
        """
        Fill database tables of goods from file data
        :param list_from_file: data from file
        :type list_from_file: list
        :return: Function return False if list_from_file empty, else True
        """

        logging.info("Формирование списка GoodInfoList")

        if len(list_from_file) == 0:
            logging.error("После прочтений из файла получился пустой список")
            return False

        for product in list_from_file:
            product_data = product.split(":")
            
            if len(product_data) != 5:
                logging.error("Следующая строка не была обработана1: {product}".format(
                              product=product))
                continue

            name_product = product_data[0]
            price_product = product_data[1]
            product_amount = product_data[2]
            product_date =  product_data[3]
            shelf_life = product_data[4]
            date_manufacture = product_data[3]

            self.add(GoodInfo(name_product, 
                              price_product, 
                              product_amount, 
                              product_date, 
                              shelf_life, 
                              date_manufacture))
        
        return True

    def add_record_shelf(self, shelf_life):
        """
        Add shelf life in table
        shelfs life
        :param shelf_life: shelf_life good
        :type shelf_life: Integer
        """
        shelf = Shelf(
            shelf_life=shelf_life
        )

        self.session.add(shelf)
        self.session.commit()

    def add_record_delivery(self, date_delivery):
        """
        Add record delivery in table
        delivery dates       
        :param date_delivery: date_delivery good
        :type date_delivery: Date
        """

        delivery = Delivery(
            date_delivery=date_delivery
        )

        self.session.add(delivery)
        self.session.commit()

    def add_record_provider(self, name):
        """
        Add record provider in table
        providers    
        :param name: name good
        :type name: String
        """

        provider = Provider(
            name=name
        )

        self.session.add(provider)
        self.session.commit()
    
    def add_record_good(self, name, amount, price, 
                        id_provider, id_shelf):
        """
        Add record good in table
        goods    
        :param name: name good
        :type name: String
        :param amount: amount good
        :type amount: Integer
        :param price: price good
        :type price: Integer
        :param id_provider: id provider in table
        :type id_provider: integer
        :param id_date: id date in table
        :type id_date: Date
        :param id_shelf: id shelf in table
        :type id_shelf: Integer
        """

        good = Good(
            name=name,
            amount=amount,
            price=price,
            id_provider=id_provider,
            id_shelf=id_shelf
        )

        self.session.add(good)
        self.session.commit()

    def get_id_provider_by_name(self, name):
        """
        Function return id by name
        :return: id provider
        :return: Integer
        """

        providers = self.session.query(Provider).filter(
                                                Provider.name == name
        )
        
        id = None

        for provider in providers:
            id = provider.id
            break
            
        return id
    
    def get_id_delivery_by_date(self, date_delivery):
        """
        Function return id by date
        :return: id date_delivery
        :return: Integer
        """

        dates = self.session.query(Delivery).filter(
                                        Delivery.date_delivery == date_delivery
        )

        id = None

        for date in dates:
            id = date.id
            break
        
        return id
    
    def get_id_shelf(self, shelf_life):
        """
        Function return id by shelf_life
        :return: id shelf_life
        :return: Integer
        """

        shelfs = self.session.query(Shelf).filter(
                                    Shelf.shelf_life == shelf_life
        )

        id = None

        for shelf in shelfs:
            id = shelf.id
            break

        return id