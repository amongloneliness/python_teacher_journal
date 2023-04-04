from modules.database.defines import *
from prettytable import PrettyTable


# Вывод списка предметов.
def print_subjects(db):
    th = ['id', 'предмет']
    td = []

    subject_id = 0

    for subject in db[DB_SUBJECTS]:
        td.append([subject_id, subject])
        subject_id += 1

    table = PrettyTable(th)

    for row in td:
        table.add_row(row)

    print(table)
    return
