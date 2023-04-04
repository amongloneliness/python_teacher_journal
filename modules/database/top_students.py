from modules.database.defines import *


# Вычисление рейтинга студентов.
def top_students(db):
    db[DB_STUDENTS_RATING] = []
    temp_dict = {}

    # Создаем ключ рейтинга для всех студентов.
    for student in db[DB_STUDENTS]:
        temp_dict[student] = 0

    # Считаем сумму оценок по каждому студенту.
    for student, subjects in db[DB_GRADES].items():
        for subject, dates in db[DB_GRADES][student].items():
            for date, grade in db[DB_GRADES][student][subject].items():
                if str.isalpha(str(grade)):
                    temp_dict[student] += 0
                else:
                    temp_dict[student] += int(grade)

    # Добаление значений в массив для сортировки.
    for student, rate in temp_dict.items():
        db[DB_STUDENTS_RATING].append([rate, student])

    # Сортировка массива.
    db[DB_STUDENTS_RATING].sort(reverse=True)

    return
