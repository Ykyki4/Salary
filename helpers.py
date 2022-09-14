import requests
from terminaltables import AsciiTable

def tableter(vacancies_info, title):
    table_data = [
        ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"]
    ]
    for key in vacancies_info:
         table_data.append([key,
                            vacancies_info[key]["vacancies_found"],
                            vacancies_info[key]["vacancies_processed"],
                            vacancies_info[key]["average_salary"]])
    table = AsciiTable(table_data, title)
    return table.table

def requester(params, url, headers=None):
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def predict_rub_salary(is_hh, vacanci):
    if is_hh:
        salary_from = vacanci["salary"]["from"]
        salary_to = vacanci["salary"]["to"]
    else:
        salary_from = vacanci["payment_from"]
        salary_to = vacanci["payment_to"]


    if salary_from is None:
        return salary_to * 0.8
    elif salary_to is None:
        return salary_from * 1.2
    else:
        return (salary_from + salary_to) / 2