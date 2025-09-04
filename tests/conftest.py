import pytest

from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy

@pytest.fixture
def vacancy_api_1():
    return HeadHunterAPI(
        base_url='https://api.hh.ru/vacancies',
        headers={"User-Agent": "Custom-Agent"}
    )

@pytest.fixture
def vacancy_api_2():
    return HeadHunterAPI(
        base_url='https://api.hh.ru/vacancies',
    )

@pytest.fixture
def vacancy_1():
    return Vacancy(
        name='Тестировщик Python',
        url='https://hh.ru/vacancy/1',
        salary=140000,
    )

@pytest.fixture
def vacancy_2():
    return Vacancy(
        name='Разработчик Python',
        url='https://hh.ru/vacancy/2',
        salary=120000,
        description='Удаленная работа'
    )

@pytest.fixture
def vacancy_error_1():
    return Vacancy(
        url='https://hh.ru/vacancy/err1',
        salary=120000
    )

@pytest.fixture
def vacancy_error_2():
    return Vacancy(
        name='Разработчик Python',
        url='https://hh.ru/vacancy/err2',
        salary=-120000
    )