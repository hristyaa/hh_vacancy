import json
import os
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

    def __init__(self, filename="vacancies.json"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        directory = os.path.join(base_dir, "data")
        os.makedirs(directory, exist_ok=True)

        self.__filename = os.path.join(directory, filename)

        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def __load(self):
        """Метод для загрузки данных из JSON-файла и преобразования их в Python-объект"""
        if os.path.getsize(self.__filename) == 0:
            return []
        with open(self.__filename, "r", encoding="utf-8") as file:
            try:

                return json.load(file)
            except json.JSONDecodeError:
                return []

    def __dump(self, data):
        """Метод преобразования Python-объекта в формат JSON и записи его в файл"""
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в JSON-файл"""
        data = self.__load()

        vacancy_dict = {
            "name": vacancy.name,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "description": vacancy.description,
        }

        if vacancy_dict not in data:
            data.append(vacancy_dict)
            self.__dump(data)

    def add_vacancies(self, vacancies):
        """Добавление списка вакансий"""
        data = self.__load()

        for vacancy in vacancies:
            vacancy_dict = {
                "name": vacancy.name,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "description": vacancy.description,
            }
            if vacancy_dict not in data:
                data.append(vacancy_dict)

        self.__dump(data)

    def get_vacancies(self, filter_words=None):
        """Получение вакансий по ключевым словам"""
        data = self.__load()
        filtered_vacancy = []

        for vacancy in data:
            name = vacancy.get("name").lower()
            description = vacancy.get("description").lower()

            if filter_words is not None:
                if any(word.lower() in name or word.lower() in description for word in filter_words):
                    filtered_vacancy.append(vacancy)
            else:
                return data
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

    def delete_vacancy(self):
        """Удаление информации о вакансиях из файла"""
        with open(self.__filename, "w") as file:
            file.write("")
