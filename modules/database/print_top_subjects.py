from prettytable import PrettyTable
from modules.database.defines import *


# Вывод топ 10 самых сложных предметов.
def print_top_subjects(db):
    th = ['предмет', 'место в рейтинге']
    td = []
    number_of_subject = 1

    for subject in db[DB_SUBJECTS_RATING]:
        if number_of_subject == 11:
            break

        td.append([subject[1], number_of_subject])
        number_of_subject += 1

    table = PrettyTable(th)

    for row in td:
        table.add_row(row)

    print(table)
