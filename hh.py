from helpers import *
from dotenv import load_dotenv
import os


def vacanci_counter(url):
    vacanci_info = {}
    page_num = 99
    languages = ["Python", "Java", "JavaScript", "C++", "C#", "1C", "C"]
    for language in languages:
        vacanci_salary_list = []
        average_salary = 0
        page = 0
        while page < page_num:
            params = {
                "text": f"Программист {language}",
                "area": 1,
                "page": page
            }
            for vacanci in requester(params, url)["items"]:
                if vacanci["salary"] is None:
                    continue
                vacanci_salary_list.append(predict_rub_salary(is_hh, vacanci))
            page += 1
            average_salary = sum(vacanci_salary_list) // len(vacanci_salary_list)

        vacanci_info[language] = {
            "vacancies_found": requester(params, url)["found"],
            "vacancies_processed": len(vacanci_salary_list),
            "average_salary": average_salary}

    return vacanci_info


if __name__ == "__main__":
    load_dotenv()
    title = "HeadHunter Moscow"
    is_hh = True
    url = os.environ['HH_URL']
    print(tableter(vacanci_counter(url), title))