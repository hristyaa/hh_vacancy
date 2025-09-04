class Vacancy():

    __slots__ = ('name', 'url', 'salary', 'description')

    def __init__(self, name, url, salary, description=None):
        self.name =self.__validate_name(name)
        self.url = self.__validate_url(url)
        self.salary = self.__validate_salary(salary)
        self.description = self.__validate_description(description)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.url}, {self.salary}, {self.description})'

    def __str__(self):
        return f"Название вакансии: {self.name}, зарплата: {self.salary}"

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
            raise ValueError('Название вакансии не указано')
        return name

    @staticmethod
    def __validate_url(url):
        if not url or 'https' not in url:
            raise ValueError('Ссылка отсутствует или неверно указана')
        return url

    @staticmethod
    def __validate_salary(salary):
        if not salary or salary < 0:
            return 0
        return salary

    @staticmethod
    def __validate_description(description):
        return description if description else "Описание отсутствует"
