from helpers import requester, tableter, predict_rub_salary
from dotenv import load_dotenv
import os


def vacanci_counter(url, secret_token):
    headers = {"X-Api-App-Id": secret_token}
    languages = ["Python", "Java", "JavaScript", "C++", "C#", "1C", "C"]
    vacancies_info = {}
    for language in languages:
        vacanci_salary_list = []
        page = 0
        average_salary = 0
        is_more = True
        while is_more:
            params = {
                        "town": 4,
                        "catalogues": 48,
                        "keyword": f"Программист {language}",
                        "no_agreement": 1,
                        "page": page
                    }
            page+=1
            response = requester(params, url, headers)
            is_more = response["more"]
            for vacanci in response["objects"]:
                vacanci_salary_list.append(predict_rub_salary(is_hh, vacanci))
            average_salary = sum(vacanci_salary_list) // len(vacanci_salary_list)
        vacancies_info[language] = {
            "vacancies_found": response["total"],
            "vacancies_processed": len(vacanci_salary_list),
            "average_salary": average_salary}
    return vacancies_info


if __name__ == "__main__":
    load_dotenv()
    secret_token = os.environ['SUPERJOB_TOKEN']
    url = "https://api.superjob.ru/2.0/vacancies/"
    title = "Superjob"
    is_hh = False
    print(tableter(vacanci_counter(url, secret_token), title))