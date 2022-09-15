from helpers import predict_rub_salary, make_table
import requests


def count_vacancy_salary(url):
    moscow_area_id = 1
    average_languages_salaries = {}
    page_num = 99
    languages = ["Python", "Java", "JavaScript", "C++", "C#", "1C", "C"]
    for language in languages:
        language_salaries = []
        average_salary = 0
        page = 0
        while page < page_num:
            params = {
                "text": f"Программист {language}",
                "area": moscow_area_id,
                "page": page
            }
            response_json = requests.get(url, params=params)
            response_json.raise_for_status()
            hh_api_response = response_json.json()
            for vacancy in hh_api_response["items"]:
                if vacancy["salary"]:
                    salary_to = vacancy["salary"]["to"]
                    salary_from = vacancy["salary"]["from"]
                    language_salaries.append(
                        predict_rub_salary(salary_from=salary_from, salary_to=salary_to))
            page += 1
        if len(language_salaries) != 0:
            average_salary = sum(language_salaries) // len(language_salaries)

        average_languages_salaries[language] = {
            "vacancies_found": hh_api_response["found"],
            "vacancies_processed": len(language_salaries),
            "average_salary": average_salary,
        }

    return average_languages_salaries


if __name__ == "__main__":
    title = "HeadHunter Moscow"
    is_hh = True
    url = "https://api.hh.ru/vacancies"
    print(make_table(count_vacancy_salary(url), title))
