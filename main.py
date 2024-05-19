from config import config
from src.utils import get_hh_data, create_database, save_data_to_database
from src.db_manager import DBManager


def main():
    print("В рамках программы Вы получите данные о вакансиях в 10 крупных IT - компаниях, размещенных на сайте HH.ru")
    print("Начинаем формирование БД с актуальными вакансиями\n")
    api_hh_ru = 'https://api.hh.ru/vacancies'
    company_ids = {'1740',  # Яндекс
                   '78638',  # Тинькофф
                   '3529',  # Сбербанк
                   '1993194',  # YADRO
                   '26624',  # Positive Technologies
                   '84585',  # Авито
                   '15478',  # VK
                   '8550',  # Центр финансовых технологий
                   '633069',  # Selectel
                   '1057'  # Лаборатория Касперского
                   }

    params = config()

    data = get_hh_data(api_hh_ru, company_ids)
    create_database('hh_data', params)
    save_data_to_database(data, 'hh_data', params)
    print("Формирование БД успешно завершено")
    while True:
        user_answer = int(input("\nКакая информация о вакасиях Вас интересует:\n"
                                "1 - Список всех компаний и количество вакансий у каждой компании\n"
                                "2 - Список всех вакансий\n"
                                "3 - Средняя зарплата по вакансиям\n"
                                "4 - Список вакансий с зарплатой выше средней\n"
                                "5 - Список вакансий по ключевому слову\n"
                                "0 - Выход из программы\n"
                                "Введите цифру: \n"))

        db_manager = DBManager()

        if user_answer == 1:
            db_manager.get_companies_and_vacancies_count('hh_data', params)
        elif user_answer == 2:
            db_manager.get_all_vacancies('hh_data', params)
        elif user_answer == 3:
            db_manager.get_avg_salary('hh_data', params)
        elif user_answer == 4:
            db_manager.get_vacancies_with_higher_salary('hh_data', params),
        elif user_answer == 5:
            user_word = input("Введите слово для поиска: ")
            db_manager.get_vacancies_with_keyword('hh_data', params, user_word)
        elif user_answer == 0:
            break


if __name__ == '__main__':
    main()
