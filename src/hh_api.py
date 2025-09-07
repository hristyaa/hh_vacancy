from abc import ABC, abstractmethod

import requests
from requests.exceptions import RequestException


class VacancyAPI(ABC):
    """
    Класс для работы с API сервисами по получению ваканский
    Класс VacancyAPI является абстрактным классом
    """

    def __init__(self, base_url, headers):
        """Инициализация класса VacancyAPI"""
        self.__base_url = base_url
        self.__headers = headers or {"User-Agent": "API-User-Agent"}

    def __connect_to_api(self, params=None):
        """Метод подключения к API"""
        try:
            response = requests.get(self.__base_url, headers=self.__headers, params=params)

            if response.status_code != 200:
                raise RequestException(f"Ошибка API запроса : {response.status_code}")

            return response.json()

        except RequestException as e:
            print(str(e))
            return None

    def get_vacancies(self, keyword):
        """Метод для получения вакансий"""
        return self.__load_vacancies(keyword)

    @abstractmethod
    def __load_vacancies(self, keyword):
        pass


class HeadHunterAPI(VacancyAPI):
    """
    Класс для работы с API HeadHunter
    Класс VacancyAPI является родительским классом
    """

    def __init__(self, base_url="https://api.hh.ru/vacancies", headers=None):
        """Инициализация класса HeadHunterAPI"""
        self.headers = headers or {"User-Agent": "HH-User-Agent"}
        super().__init__(base_url, headers)
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def __str__(self):
        # Печатаем количество найденных вакансий
        return f"HeadHunterAPI (Найдено вакансий: {len(self.__vacancies)})"

    def _VacancyAPI__load_vacancies(self, keyword):
        """Метод для получения вакансий по ключевому слову"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            # response = requests.get(self.__base_url, headers=self.headers, params=self.__params)
            response = self._VacancyAPI__connect_to_api(self.__params)
            vacancies = response["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1
        return self.__vacancies


# hh_api = HeadHunterAPI()
# # Пример ключевого слова для поиска вакансий
# keyword = 'Python'
#
# # Получаем вакансии
# vacancies = hh_api.get_vacancies(keyword=keyword)
#
# # Проверяем, что вакансии были получены
# if vacancies:
#     print(f"Найдено {len(vacancies)} вакансий по запросу '{keyword}':")
#     for vacancy in vacancies[:5]:  # Выводим первые 5 вакансий
#         print(f" - {vacancy['name']} (Компания: {vacancy['employer']['name']})")
# else:
#     print(f"Вакансии по запросу '{keyword}' не найдены.")


# # Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
#
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies(keyword="Python")
#
# print(hh_vacancies)

# print(hh_vacancies)
