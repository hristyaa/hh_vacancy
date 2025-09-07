from src.file_saver import JSONSaver
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    """
    Функция для взаимодействия с пользователем через консоль. Данная функция реализует:

    Ввод поискового запроса для запроса вакансий из hh.ru;
    Получение топ N вакансий по зарплате (N запрашивает у пользователя);
    Пллучение вакансии с ключевым словом в описании.

    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON по запросу
    hh_vacancies = hh_api.get_vacancies(search_query)
    print(hh_api)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_saver = JSONSaver()
    json_saver.add_vacancies(vacancies_list)

    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)
    sorted_vacancies = Vacancy.sort_vacancies(filtered_vacancies)
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)

    for vacancy in top_vacancies:
        print(vacancy)
        print()
    print(f"Все вакансии по поисковому запросу сохранены в {json_saver._JSONSaver__filename}")
    user_input = input("Желаете очистить файл? да/нет\n")
    if user_input == "да":
        json_saver = JSONSaver()
        json_saver.delete_vacancy()
        print("Файл очищен")
    else:
        print("Файл не будет очищен")
    print("Всего хорошего!")


# if __name__ == "__main__":
#     user_interaction()
