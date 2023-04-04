from modules.database.defines import *


# Создание пустой учебной базы данных.
def create_empty_db():
    db = {
        DB_STUDENTS: [],
        DB_SUBJECTS: [],
        DB_GRADES: {}
    }

    return db
