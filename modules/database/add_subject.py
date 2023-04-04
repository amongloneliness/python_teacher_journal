from modules.database.defines import *


# Добавление предмета в учебную базу.
def add_subject(subject_name, db):
    # Проверка, содержится ли предмет в учебной базе.
    if subject_name in db[DB_SUBJECTS]:
        print(f'\nПредмет {subject_name} уже содержится в учебной базе данных.\n')
        return False
    else:
        db[DB_SUBJECTS].append(subject_name)

    # Добавление пустого словаря [оценок по новому предмету] каждому студенту.
    for student in db[DB_GRADES]:
        db[DB_GRADES][student][subject_name] = {}

    return True
