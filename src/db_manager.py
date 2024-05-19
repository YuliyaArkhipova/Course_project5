import psycopg2


class DBManager:

    @staticmethod
    def get_companies_and_vacancies_count(db_name: str, params: dict) -> None:
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT company_name, COUNT(name) AS vacancies FROM vacancies
                GROUP BY company_name
                """)
            rows = cur.fetchall()
            print("\nСписок компаний и количество вакансий:\n")
            for row in rows:
                print(f"Название компании - {row[0]}\nКоличество открытых вакансий - {row[1]}\n")

        conn.close()

    @staticmethod
    def get_all_vacancies(db_name: str, params: dict) -> None:
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT company_name, name, salary, vacancy_url FROM vacancies
                """)
            rows = cur.fetchall()
            print("\nСписок всех вакансий:\n")
            for row in rows:
                print(f"Название компании - {row[0]}\n"
                      f"Название вакансии  - {row[1]}\n"
                      f"Зарплата - {"Зарплата не указана" if row[2] is None else row[2]}\n"
                      f"Ссылка на вакансию - {row[3]}\n")

        conn.close()

    @staticmethod
    def get_avg_salary(db_name: str, params: dict) -> None:
        """
        Получает среднюю зарплату по вакансиям.
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT AVG(salary) FROM vacancies
                """)
            rows = cur.fetchall()
            for row in rows:
                print(f"\nСредняя зарплата по вакансиям - {row[0]}")

        conn.close()

    @staticmethod
    def get_vacancies_with_higher_salary(db_name: str, params: dict) -> None:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT company_name, name, salary, vacancy_url FROM vacancies
                WHERE salary IS NOT NULL
                AND salary > (SELECT AVG(salary) FROM vacancies)
                """)
            rows = cur.fetchall()
            print("\nВакансии с зарплатой выше средней по всем вакансиям:\n")
            for row in rows:
                print(f"Название компании - {row[0]}\n"
                      f"Название вакансии  - {row[1]}\n"
                      f"Зарплата - {row[2]}\n"
                      f"Ссылка на вакансию - {row[3]}\n")

        conn.close()

    @staticmethod
    def get_vacancies_with_keyword(db_name: str, params: dict, user_word: str) -> None:
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова,
        например Python.
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM vacancies "
                        f"WHERE name LIKE '{user_word.capitalize()}%'")
            rows = cur.fetchall()
            print("\nСписок найденных вакансий\n")
            for row in rows:
                print(f"Название компании - {row[2]}\n"
                      f"Название вакансии  - {row[1]}\n"
                      f"Зарплата - {"Зарплата не указана" if row[3] is None else row[3]}\n"
                      f"Ссылка на вакансию - {row[4]}\n")

        conn.close()
