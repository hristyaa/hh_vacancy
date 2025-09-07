from src.utils import strip_tags


class Vacancy:

    __slots__ = ("name", "url", "salary", "description")

    def __init__(self, name, url, salary, description=None):
        self.name = self.__validate_name(name)
        self.url = self.__validate_url(url)
        self.salary = self.__validate_salary(salary)
        self.description = self.__validate_description(description)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.url}, {self.salary}, {self.description})"

    def __str__(self):
        return (
            f"Вакансия: {self.name}\n"
            f"Ссылка: {self.url}\n"
            f"Зарплата: {self.salary}\n"
            f"Описание: {self.description}\n"
            f"{'-' * 3}"
        )

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    @staticmethod
    def __validate_name(name):
        if not name:
            raise ValueError("Название вакансии не указано")
        return name

    @staticmethod
    def __validate_url(url):
        if not url or "https" not in url:
            raise ValueError("Ссылка отсутствует или неверно указана")
        return url

    @staticmethod
    def __validate_salary(salary):
        if salary is None:
            return 0
        if isinstance(salary, dict):

            _from = salary.get("from") or 0
            _to = salary.get("to") or 0
            _currency = salary.get("currency")

            if _currency != "RUR":
                return 0
            if _from == 0 and _to != 0:
                return _to
            return _from
        if isinstance(salary, int) and salary >= 0:
            return salary
        return 0

    @staticmethod
    def __validate_description(description):
        return description if description else "Описание отсутствует"

    @classmethod
    def cast_to_object_list(cls, data):
        """Преобразование списка словарей (из JSON) в список объектов Vacancy"""
        vacancies = []
        for item in data:
            snippet = item.get("snippet", {})
            requirement = snippet.get("requirement", "")
            responsibility = snippet.get("responsibility", "")

            description = f"{requirement} {responsibility}".strip()

            vacancies.append(
                cls(
                    name=item.get("name"),
                    url=item.get("url"),
                    salary=item.get("salary"),
                    description=strip_tags(description),
                )
            )
        return vacancies

    @staticmethod
    def filter_vacancies(vacancies, keywords):
        """Фильтрует вакансии по ключевым словам в описании"""
        filtered = []
        for vacancy in vacancies:
            if any(word.lower() in vacancy.description.lower() for word in keywords):
                filtered.append(vacancy)
        return filtered

    @staticmethod
    def sort_vacancies(vacancies):
        """Возвращает отсортированные по зарплате вакансии"""

        sorted_vacancies = sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)

        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(sorted_vacancies, n):
        """Возвращает топ n вакансий"""

        top_vacancies = sorted_vacancies[:n]
        return top_vacancies
