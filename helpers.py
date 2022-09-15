from terminaltables import AsciiTable


def make_table(vacancies_salary, title):
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
    if not salary_from:
        return salary_to * 0.8
    elif not salary_to:
        return salary_from * 1.2
    else:
        return (salary_from + salary_to) / 2