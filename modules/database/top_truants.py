from modules.database.defines import *


# Вычисление прогулов студентов.
def top_truants(db):
    db[DB_STUDENTS_SKIPPING] = []
    temp_dict = {}

    # Создаем ключ рейтинга для всех студентов.
    for student in db[DB_STUDENTS]:
        temp_dict[student] = 0

    # Считаем сумму оценок по каждому студенту.
    for student, subjects in db[DB_GRADES].items():
        for subject, dates in db[DB_GRADES][student].items():
            for date, grade in db[DB_GRADES][student][subject].items():
                if str(grade) == 'н':
                    temp_dict[student] += 1
                else:
                    temp_dict[student] += 0

    # Добаление значений в массив для сортировки.
    for student, skipping in temp_dict.items():
        db[DB_STUDENTS_SKIPPING].append([skipping, student])

    # Сортировка массива.
    db[DB_STUDENTS_SKIPPING].sort(reverse=True)

    return
