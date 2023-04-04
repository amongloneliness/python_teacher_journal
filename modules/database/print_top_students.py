from prettytable import PrettyTable
from modules.database.defines import *


# Вывод топ 10 студентов с лучшей успеваемостью.
def print_top_students(db):
    th = ['студент', 'место в рейтинге']
    td = []
    number_of_student = 1

    for student in db[DB_STUDENTS_RATING]:
        if number_of_student == 11:
            break

        td.append([student[1], number_of_student])
        number_of_student += 1

    table = PrettyTable(th)

    for row in td:
        table.add_row(row)

    print(table)
