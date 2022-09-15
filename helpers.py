import requests
from terminaltables import AsciiTable


def maker_tablet(vacancies_salary, title):
    vacancy_salary_table = [
        ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"]
    ]
    for language in vacancies_salary:
         vacancy_salary_table.append([language,
                            vacancies_salary[language]["vacancies_found"],
                            vacancies_salary[language]["vacancies_processed"],
                            vacancies_salary[language]["average_salary"]])
    table = AsciiTable(vacancy_salary_table, title)
    return table.table


def predict_rub_salary(salary_from, salary_to):
    if salary_from is None:
        return salary_to * 0.8
    elif salary_to is None:
        return salary_from * 1.2
    else:
        return (salary_from + salary_to) / 2