from modules.database.defines import *


# Добавление оценки в учебную базу.
def add_grade(
    student,   # студент учреждения
    subject,   # учебный предмет
    grade,     # оценка по предмету
    date,      # дата получения оценки
    db         # учебная база данных
):
    # Проверка наличия студента и предмета.
    if not (student in db[DB_STUDENTS]):
        print(f'Студента {student} нет в базе!\n')
        return
    elif not (subject in db[DB_SUBJECTS]):
        print(f'Предмета {subject} нет в базе!\n')
        return

    db[DB_GRADES][student][subject][str(date)] = grade

    return
