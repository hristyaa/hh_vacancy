import pytest

from src.hh_api import HeadHunterAPI


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