import os
import shutil
import logging


class FileUser:
    """
    Represents file user

    Attributes:

    path_to_file (str): path to file with goods
    file_data (file descriptor): file descriptor

    Methods: 

    __init__()
    select_file()
    save_by_directory()
    __del__()

    """

    def __init__(self):
        """
        Initilize path to file
        and file data 
        """
        self.path_to_file = ''
        self.file_data = None

    def select_path_file(self):
        """
        Function input path to file with goods
        :return: if file exists return list from file
        else function return false
        :rtype: list if file exists, false else
        """

        logging.info("Имя модуля")
        logging.info(__name__)
        logging.info("Функция select_file")        

        print("Введите путь до файла с товарами")
        
        self.path_to_file = str(input())
        self.path_to_file = os.path.abspath(self.path_to_file)

        if  os.path.isfile(self.path_to_file) and os.path.exists(self.path_to_file):
            
            self.file_data = open(self.path_to_file, "r", encoding="utf-8")
            list_from_file = self.file_data.readlines()
            return list_from_file
        
        else:
            logging.error("It is not file or file not exists")
            return False
    
    def save_by_directory(self):
        """
        Function saved filed in directory
        return: function nothing return
        """

        print("В какую директорию сохранить считанный файл?")
        
        logging.info("Имя модуля")
        logging.info(__name__)
        logging.info("Функция save_by_directory")        

        
        directory = str(input())

        if os.path.exists(directory):
            shutil.copy(self.path_to_file, directory)
        else:
            os.mkdir(directory)
            shutil.copy(self.path_to_file, directory)
    
    def __del__(self):
        """
        Function closed file
        """

        logging.info("Имя модуля")
        logging.info(__name__)
        logging.info("Функция __del__")    

        self.file_data.close()
        
