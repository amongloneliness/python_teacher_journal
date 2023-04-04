from modules.database.defines import *
from prettytable import PrettyTable


def print_db(db):
    # Заголовки таблицы.
    th = ['студент', 'предмет', 'дата оценки', 'оценка']

    # Данные таблицы.
    td = []

    columns = len(th)   # Количество столбцов таблицы.
    table = PrettyTable(th)   # Таблица данных.

    # Добавление данных из учебной базы данных.
    for student, subjects in db[DB_GRADES].items():
        for subject, dates in subjects.items():
            for date, grade in dates.items():
                td.append([student, subject, date, grade])

    # Добавление данных в таблицу.
    for row in td:
        table.add_row(row)

    # Вывод таблицы.
    print(table)

    return
