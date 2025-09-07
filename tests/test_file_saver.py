import json

from src.file_saver import JSONSaver
from src.vacancy import Vacancy


def test_file_saver_init(tmp_path):
    """Тест на иницаилизацию класса JSONSaver"""
    filename = tmp_path / "test_vacancies.json"

    # создаем объект
    saver = JSONSaver(filename=str(filename))

    # проверяем что файл создался
    assert filename.exists()

    # проверяем что файл пустой (в нем список [])
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == []

    # проверяем что get_vacancies возвращает пустой список
    vacancies = saver.get_vacancies()
    assert vacancies == []


def test_add_vacancy(tmp_path):
    """Тест на добавление вакансии"""
    filename = tmp_path / "test_vacancies.json"
    saver = JSONSaver(filename=str(filename))

    # Создаем объект Vacancy
    vacancy = Vacancy(
        name="Python Developer", url="https://hh.ru/vacancy/123", salary=150000, description="Опыт работы с Django"
    )

    # Добавляем вакансию
    saver.add_vacancy(vacancy)

    # Проверяем, что файл не пустой
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"
    assert data[0]["salary"] == 150000
    assert data[0]["url"] == "https://hh.ru/vacancy/123"
    assert data[0]["description"] == "Опыт работы с Django"

    # Проверяем, что дубликаты не добавляются
    saver.add_vacancy(vacancy)
    with open(filename, "r", encoding="utf-8") as f:
        data_after = json.load(f)

    assert len(data_after) == 1  # дубликат не записан


def test_add_vacancies(tmp_path, hh_vacancies_Vacancy):
    """Тест на добавление вакансий"""
    filename = tmp_path / "test_vacancies.json"
    saver = JSONSaver(filename=str(filename))

    # Создаем объект Vacancy
    vacancies = hh_vacancies_Vacancy

    # Добавляем вакансию
    saver.add_vacancies(vacancies)

    # Проверяем, что файл не пустой
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Python Developer"
    assert data[0]["salary"] == 120000
    assert data[0]["url"] == "https://hh.ru/vacancy/123"
    assert data[0]["description"] == "Опыт работы с Django. Разработка веб-сервисов"

    # Проверяем, что дубликаты не добавляются
    saver.add_vacancies(vacancies)
    with open(filename, "r", encoding="utf-8") as f:
        data_after = json.load(f)

    assert len(data_after) == 2  # дубликат не записан
