from modules.database.load_from_json import *
from modules.database.defines import *


# Создание БД, используя Json.
def create_db():
    # Объект учебной базы данных.
    db = {}

    # Загрузка json данных.
    students = load_from_json(DB_STUDENTS_JSON)[DB_STUDENTS]
    subjects = load_from_json(DB_SUBJECTS_JSON)[DB_SUBJECTS]
    grades = load_from_json(DB_GRADES_JSON)[DB_GRADES]

    # Проверка студентов.
    if len(students) != 0:
        db[DB_STUDENTS] = students
    else:
        db[DB_STUDENTS] = []

    # Проверка учебных предметов.
    if len(subjects) != 0:
        db[DB_SUBJECTS] = subjects
    else:
        db[DB_SUBJECTS] = []

    # Проверка оценок
    if len(grades) != 0:
        db[DB_GRADES] = grades
    else:
        db[DB_GRADES] = {}

        for student in students:
            db[DB_GRADES][student] = {}

            for subject in subjects:
                db[DB_GRADES][student][subject] = {}

    return db
