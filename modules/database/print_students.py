from modules.database.defines import *
from prettytable import PrettyTable


# Вывод студентов.
def print_students(db):
    # Заголовки / данные таблицы.
    th = ['id', 'студент']
    td = []

    student_id = 0

    for student in db[DB_STUDENTS]:
        td.append([student_id, student])
        student_id += 1

    table = PrettyTable(th)

    for row in td:
        table.add_row(row)

    print(table)
    return
