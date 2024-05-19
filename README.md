# Курсовой проект по курсу «Работа с базами данных»

#### В рамках проекта Вы получаете данные о 10 IT- компаниях и вакансиях с сайта hh.ru:   
_Яндекс_, _Тинькофф_, _Сбербанк_, _YADRO_, _Positive Technologies_,
_Авито_, _VK_, _Центр финансовых технологий_, _Selectel_, _Лаборатория Касперского_
#### создаете таблицы в БД PostgreSQL и загружаете полученные данные в созданные таблицы.

### Из созданной БД PostgreSQL программа позволяет получить по запросу пользователя информацию о вакансиях:
 1 - Список всех компаний и количество вакансий у каждой компании   
 2 - Список всех вакансий   
 3 - Средняя зарплата по вакансиям   
 4 - Список вакансий с зарплатой выше средней   
 5 - Список вакансий по ключевому слову   
                                
## Инструкция по запуску
1. Клонируйте данный репозиторий на свой локальный компьютер

`git clone https://github.com/YuliyaArkhipova/Course_project5`  

2. Установите виртуальное окружение

`python3 -m venv venv`

3. Активируйте виртуальное окружение
   
Windows: `venv\Scripts\activate`  
macOS и Linux: `source venv/bin/activate` 

4. Установите необходимые для работы библиотеки, указанные в requirements.txt
   
`python -m pip install -r requirements.txt`  

5. Заполните файл database.ini
   
6. Для включения в программу другой компаний, необходимо добавить ее ID в переменную `company_ids`

7. Запустите 'main.py'



