from modules.database.defines import *


# Вывод топ 10 самых трудных учебных предметов.
def top_subjects(db):
    db[DB_SUBJECTS_RATING] = []
    temp_dict = {}

    # Создаем ключ рейтинга для всех студентов.
    for subject in db[DB_SUBJECTS]:
        temp_dict[subject] = 0

    # Считаем сумму оценок по каждому студенту.
    for student, subjects in db[DB_GRADES].items():
        for subject, dates in db[DB_GRADES][student].items():
            for date, grade in db[DB_GRADES][student][subject].items():
                if str.isalpha(str(grade)):
                    temp_dict[subject] += 0
                else:
                    temp_dict[subject] += int(grade)

    # Добаление значений в массив для сортировки.
    for subject, rate in temp_dict.items():
        db[DB_SUBJECTS_RATING].append([rate, subject])

    # Сортировка массива.
    db[DB_SUBJECTS_RATING].sort()

    return
