from helpers import *


def counter_vacancy_salary(url):
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
            response = requests.get(url, params=params)
            response.raise_for_status()
            response_json = response.json()
            for vacancy in response_json["items"]:
                if vacancy["salary"] is None:
                    continue
                salary_to = vacancy["salary"]["to"]
                salary_from = vacancy["salary"]["from"]
                language_salaries.append(
                    predict_rub_salary(salary_from=salary_from, salary_to=salary_to))
            page += 1
            print(language_salaries)
        if len(language_salaries) == 0:
            continue
        average_salary = sum(language_salaries) // len(language_salaries)
        print(average_salary)

        average_languages_salaries[language] = {
            "vacancies_found": response_json["found"],
            "vacancies_processed": len(language_salaries),
            "average_salary": average_salary,
        }

    return average_languages_salaries


if __name__ == "__main__":
    title = "HeadHunter Moscow"
    is_hh = True
    url = "https://api.hh.ru/vacancies"
    print(maker_tablet(counter_vacancy_salary(url), title))