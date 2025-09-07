import os
import json
from abc import ABC, abstractmethod


class FileSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, **kwargs):
        pass


class JSONSaver(FileSaver):
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename='vacancies.json'):
        self.__filename = os.path.join("../data", filename)

        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def __load(self):
        """Метод для загрузки данных из JSON-файла и преобразования их в Python-объект"""
        with open(self.__filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def __dump(self, data):
        """Метод преобразования Python-объекта в формат JSON и записи его в файл"""
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансий в JSON-файл"""
        data = self.__load()

        vacancy_dict = {
            "name": vacancy.name,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "description": vacancy.description
        }

        if vacancy_dict not in data:
            data.append(vacancy_dict)
            self.__dump(data)

    def get_vacancies(self, filter_words=None):
        """Получение вакансий по ключевым словам"""
        data = self.__load()
        filtered_vacancy = []

        for vacancy in data:
            name = vacancy.get('name').lower()
            description = vacancy.get('description').lower()

            if filter_words is not None:
                if any(word.lower() in name or word.lower() in description for word in filter_words):
                    filtered_vacancy.append(vacancy)
        return filtered_vacancy

        # for f_vacancy in filtered_vacancy:
        #     salary = int(f_vacancy.get('salary', 0))
        #     if min_salary is not None and max_salary is not None:
        #         if min_salary <= salary <= max_salary:
        #             result.append(f_vacancy)
        #
        #     elif min_salary is not None and max_salary is None:
        #         if salary >= min_salary:
        #             result.append(f_vacancy)
        #
        #     elif min_salary is None and max_salary is not None:
        #         if salary <= max_salary:
        #             result.append(f_vacancy)
        #
        # return result

    def delete_vacancy(self, vacancy_url):
        """Удаление вакансии по URL"""
        data = self.__load()
        new_data = [vacancy for vacancy in data if vacancy.get("url") != vacancy_url]
        self.__dump(new_data)


















