from prettytable import PrettyTable
from modules.database.defines import *


# Вывод топ 10 прогульщиков.
def print_top_truants(db):
    th = ['студент', 'количество прогулов']
    td = []
    number_of_student = 1

    for student in db[DB_STUDENTS_SKIPPING]:
        if number_of_student == 11:
            break

        td.append([student[1], student[0]])
        number_of_student += 1

    table = PrettyTable(th)

    for row in td:
        table.add_row(row)

    print(table)
