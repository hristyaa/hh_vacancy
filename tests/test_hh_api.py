import pytest
from unittest.mock import Mock, patch

from requests.exceptions import RequestException

from src.hh_api import VacancyAPI


def test_vacancy_api_init(vacancy_api_1, vacancy_api_2):
    '''Тест на инициализацию класса HeadHunterAPI'''
    assert isinstance(vacancy_api_1, VacancyAPI)
    assert vacancy_api_1._VacancyAPI__base_url == 'https://api.hh.ru/vacancies'
    assert vacancy_api_1.headers == {"User-Agent": "Custom-Agent"}
    assert vacancy_api_2._VacancyAPI__base_url == 'https://api.hh.ru/vacancies'
    assert vacancy_api_2.headers == {'User-Agent': 'HH-User-Agent'}


def test_connect_to_api(vacancy_api_1):
    """Тест на работу функции"""
    test_data = {"items":[{"id":"93353083","name":"Тестировщик Python"}]}
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = test_data

    with patch("requests.get", return_value=mock_response):
        result = vacancy_api_1._VacancyAPI__connect_to_api()
        assert result == test_data



def test_connect_to_api_error(vacancy_api_1, capsys):
    """Тест обработки ошибки API"""
    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.get", return_value=mock_response):
        result = vacancy_api_1._VacancyAPI__connect_to_api()
        assert result == None
        capsys.readouterr()
        assert 'RequestException(f"Ошибка API запроса : 500")'
        assert str(vacancy_api_1) == 'HeadHunterAPI (Найдено вакансий: 0)'

def test_get_vacancies(vacancy_api_1):
    """Тест успешного получения вакансий"""
    test_data = {"items":[{"id":"93353083","name":"Тестировщик Python"}]}

    with patch.object(vacancy_api_1, "_VacancyAPI__load_vacancies", return_value=test_data):

        vacancies = vacancy_api_1.get_vacancies(keyword="Python")
        assert isinstance(vacancies, dict)
        assert len(vacancies) > 0
        assert vacancies["items"][0]["name"] == "Тестировщик Python"
