import pytest

from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    """Тест на инициализацию класса Vacancy, тест магических методов отображения класса"""
    assert vacancy_1.name == "Тестировщик Python"
    assert vacancy_1.url == "https://hh.ru/vacancy/1"
    assert vacancy_1.salary == 140000
    assert vacancy_1.description == "Описание отсутствует"
    assert (
        str(vacancy_1)
        == """Вакансия: Тестировщик Python
Ссылка: https://hh.ru/vacancy/1
Зарплата: 140000
Описание: Описание отсутствует
---"""
    )

    assert repr(vacancy_1) == "Vacancy(Тестировщик Python, https://hh.ru/vacancy/1, 140000, Описание отсутствует)"


def test_vacancy_validate_name():
    """Тест на валидацию названия вакансии"""
    with pytest.raises(ValueError, match="Название вакансии не указано"):
        Vacancy(name=None, url="https://hh.ru/vacancy/err1", salary=120000)


def test_vacancy_validate_url():
    """Тест на валидацию ссылки на вакансию"""
    with pytest.raises(ValueError, match="Ссылка отсутствует или неверно указана"):
        Vacancy(name="Тестировщик Python", url="//hh.ru/vacancy/err1", salary=120000)

    with pytest.raises(ValueError, match="Ссылка отсутствует или неверно указана"):
        Vacancy(name="Тестировщик Python", url=None, salary=120000)


def test_vacancy_validate_salary(vacancy_salary):
    """Тест на валидацию зарплаты"""
    assert vacancy_salary.salary == 0


def test_vacancy_compare(vacancy_1, vacancy_2):
    """Тест на проверку сравнения вакансий по зарплате"""
    assert vacancy_1.__eq__(vacancy_2) is False
    assert vacancy_1.__lt__(vacancy_2) is False
    assert vacancy_1.__le__(vacancy_2) is False
    assert vacancy_1.__gt__(vacancy_2) is True
    assert vacancy_1.__ge__(vacancy_2) is True


def test_cast_to_object_list(hh_vacancies):
    result = Vacancy.cast_to_object_list(hh_vacancies)
    assert result == [
        Vacancy(
            "Python Developer", "https://hh.ru/vacancy/123", 120000, "Опыт работы с Django Разработка веб-сервисов"
        ),
        Vacancy(
            "Java Developer", "https://hh.ru/vacancy/321", 140000, "Опыт работы с Java Разработка веб-сервисов Java"
        ),
    ]
