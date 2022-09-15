from helpers import *
from dotenv import load_dotenv
import os


def counter_vacancy_salary(url, secret_token):
    moscow_town_id = 4
    it_catalogue_id = 48
    no_agreement = 1
    headers = {"X-Api-App-Id": secret_token}
    languages = ["Python", "Java", "JavaScript", "C++", "C#", "1C", "C"]
    average_languages_salaries = {}
    for language in languages:
        language_salaries = []
        page = 0
        average_salary = 0
        is_more = True
        while is_more:
            params = {
                        "town": moscow_town_id,
                        "catalogues": it_catalogue_id,
                        "keyword": f"Программист {language}",
                        "no_agreement": no_agreement,
                        "page": page
                    }
            page += 1
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            is_more = response_json["more"]
            for vacancy in response_json["objects"]:
                salary_from = vacancy["payment_from"]
                salary_to = vacancy["payment_to"]
                language_salaries.append(
                    predict_rub_salary(salary_from=salary_from, salary_to=salary_to))
        if len(language_salaries) == 0:
            continue
        average_salary = sum(language_salaries) // len(language_salaries)

        average_languages_salaries[language] = {
            "vacancies_found": response_json["total"],
            "vacancies_processed": len(language_salaries),
            "average_salary": average_salary,
        }
    return average_languages_salaries


if __name__ == "__main__":
    load_dotenv()
    secret_token = os.environ['SUPERJOB_TOKEN']
    url = "https://api.superjob.ru/2.0/vacancies/"
    title = "Superjob"
    is_hh = False
    print(maker_tablet(counter_vacancy_salary(url, secret_token), title))
