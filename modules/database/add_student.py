from modules.database.defines import *


# Добавление студента в БД.
def add_student(student_name, db):
    # Проверка, содержится ли студент в базе учеников.
    if student_name in db[DB_STUDENTS]:
        print(f'\nСтудент {student_name} уже содержится в базе учеников.\n')
        return False
    else:
        db[DB_STUDENTS].append(student_name)

    # Добавление оценок студента для каждого предмета
    db[DB_GRADES][student_name] = {}

    for subject in db[DB_SUBJECTS]:
        db[DB_GRADES][student_name][subject] = {}

    return True
