from modules.database.defines import *

# Модуль для работы с json.
import json


# Сохранить БД в json.
def save_to_json(db):
    # Сохранение списка студентов.
    with open(DB_STUDENTS_JSON, "w") as jsonfile:
        json.dump({'students': db[DB_STUDENTS]}, jsonfile, indent=4)

    # Сохранение списка предметов.
    with open(DB_SUBJECTS_JSON, "w") as jsonfile:
        json.dump({'subjects': db[DB_SUBJECTS]}, jsonfile, indent=4)

    # Сохранение оценок.
    with open(DB_GRADES_JSON, "w") as jsonfile:
        json.dump({'grades': db[DB_GRADES]}, jsonfile, indent=4)

    return
