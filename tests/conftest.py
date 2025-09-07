import pytest

from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_api_1():
    return HeadHunterAPI(base_url="https://api.hh.ru/vacancies", headers={"User-Agent": "Custom-Agent"})


@pytest.fixture
def vacancy_api_2():
    return HeadHunterAPI(
        base_url="https://api.hh.ru/vacancies",
    )


@pytest.fixture
def vacancy_1():
    return Vacancy(name="Тестировщик Python", url="https://hh.ru/vacancy/1", salary=140000)


@pytest.fixture
def vacancy_2():
    return Vacancy(
        name="Разработчик Python", url="https://hh.ru/vacancy/2", salary=120000, description="Удаленная работа"
    )


@pytest.fixture
def vacancy_salary():
    return Vacancy(name="Разработчик Python", url="https://hh.ru/vacancy/err2", salary=-120000)


@pytest.fixture
def hh_vacancies():
    return [
        {
            "name": "Python Developer",
            "url": "https://hh.ru/vacancy/123",
            "salary": {"from": 120000, "to": 150000, "currency": "RUR"},
            "snippet": {"requirement": "Опыт работы с Django", "responsibility": "Разработка веб-сервисов"},
        },
        {
            "name": "Java Developer",
            "url": "https://hh.ru/vacancy/321",
            "salary": {"from": 140000, "to": 190000, "currency": "RUR"},
            "snippet": {"requirement": "Опыт работы с Java", "responsibility": "Разработка веб-сервисов Java"},
        },
    ]
