import os
import shutil
import logging


class FileWork:
    """
    Represents work with file

    Attributes:

    path_to_file (str): path to file with goods
    file_data (file descriptor): file descriptor

    Methods: 

    __init__()
    select_file()
    save_in_directory()
    __check_is_file()
    __check_path_exists()
    __del__()

    """

    def __init__(self):
        """
        Initilize path to file
        and file data 
        """
        self.path_to_file = ''
        self.file_data = None

    def select_path_file(self, mode="user"):
        """
        Function input path to file with goods
        :param mode: default "user", use for input path,
        mode="test" use for unittest
        :return: if file exists return list from file
        else function return false
        :rtype: list if file exists, empty list else
        """
        
        if mode == "user":
            print("Введите путь до файла с товарами")
            self.path_to_file = str(input())
        elif mode == "test":
            self.path_to_file = "goods2.info"

        self.path_to_file = self.path_to_file.strip(" ' ")
        self.path_to_file = self.path_to_file.strip(' " ')
        
        self.path_to_file = os.path.abspath(self.path_to_file)

        if  self.__check_is_file() and self.__check_path_exists():
            
            self.file_data = open(self.path_to_file, "r", encoding="utf-8")
            list_from_file = self.file_data.readlines()
            return list_from_file
        
        else:
            logging.error("Это не файл или не директории не существует")
            return []
    
    def save_in_directory(self):
        """
        Function saved filed in directory
        return: function return False if file
        not defined, else return True
        """

        if self.file_data is None:
            print("Невозможно сохранить файл в директорию")
            logging.error("Невозможно сохранить файл в директорию")
            return False

        print("В какую директорию сохранить считанный файл?")
        
        name_directory = str(input())
        name_directory = name_directory.strip(" ' ")
        name_directory = name_directory.strip(' " ')

        if os.path.isfile(name_directory):
            logging.error("Вы указали файл, а не папку")
            print("Вы указали файл, а не папку")
            return False

        if  (os.path.exists(name_directory) and 
            FileWork.__check_right_write(name_directory)):
            return False

        if not os.path.exists(name_directory):
            os.makedirs(name_directory)
            shutil.copy(self.path_to_file, name_directory)
        else:
            name_file = os.path.basename(self.path_to_file)
            new_path = os.path.join(name_directory, name_file)

            file_dat1 = open(name_file, 'r')
            file_dat2 = open(new_path, 'r')
            file_d1, file_d2 = file_dat1.fileno(), file_dat2.fileno()

            if os.path.sameopenfile(file_d1, file_d2):
                logging.error("Вы должны выбрать директорию куда сохранить файл")
                print("Вы должны выбрать директорию куда сохранить файл")
                return False
            else:
                shutil.copy(self.path_to_file, name_directory)
                return True

    def __check_is_file(self):
        """
        Function checking have file to path
        :return: if file exists return true, else false
        """
        if os.path.isfile(self.path_to_file):
            return True
        else:
            logging.error("По указанному пути нет файла")
            print("По указанному пути нет файла")
            return False
    
    def __check_path_exists(self):
        """
        Function checking exists file to path
        :return: if path exists return true, else false
        """
        
        if os.path.exists(self.path_to_file):
            return True
        else:
            logging.error("По указанному пути не существует файла")
            print("По указанному пути не существует файла")
            return False

    @staticmethod
    def __check_right_write(path_directory):
        """
        Function check right write in directory
        :param path_directory: path with directorires
        :type path_directory: string
        :return: Function return True if has for write,
        False else
        """
        if os.access(path_directory, os.W_OK):
            return True
        else:
            logging.error("Нет права записывать по пути {path}".format(
                                                                path=path_directory))
            print("Нет права записывать по пути {path}".format(path=path_directory))
            return False

    def __del__(self):
        """
        Function remove object and closed file
        """

        if self.file_data is not None:
            logging.info("Удаление объекта FileWork")    
            self.file_data.close()
    
