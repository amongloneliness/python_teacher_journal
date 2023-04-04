import sys
import threading
from modules.system.clear import *
from datetime import datetime
from modules.database.save_to_json import *
from modules.database.create_db import *
from modules.database.create_empty_db import *
from modules.database.add_student import *
from modules.database.add_subject import *
from modules.database.add_grade import *
from modules.database.print_db import *
from modules.database.print_students import *
from modules.database.print_subjects import *
from modules.database.top_students import *
from modules.database.top_truants import *
from modules.database.top_subjects import *
from modules.database.print_top_students import *
from modules.database.print_top_truants import *
from modules.database.print_top_subjects import *

db = create_db()
clear()

# Потоки.
thr_top_students = threading.Thread(target=top_students, args=(db, ))
thr_top_truants = threading.Thread(target=top_truants, args=(db, ))
thr_top_subjects = threading.Thread(target=top_subjects, args=(db, ))

# Запуск потоков.
thr_top_students.start()
thr_top_truants.start()
thr_top_subjects.start()


# Рекурсивная функция работы программы.
def start(arg):
    global db
    global thr_top_students
    global thr_top_truants
    global thr_top_subjects

    # Проверка выбора пользователя.
    if (arg >= 1) and (arg <= 12):
        # Вывод всех таблиц.
        if arg == DB_PRINT_ALL:
            print_students(db)
            print()
            print_subjects(db)
            print()
            print_db(db)

        # Добавление студента.
        elif arg == DB_ADD_STUDENT:
            thr_top_students.join()
            thr_top_truants.join()
            thr_top_subjects.join()

            print_students(db)
            add_student(input('\nВведите имя студента: '), db)
            clear()

            # Обновление данных о рейтингах.
            thr_top_students = threading.Thread(target=top_students, args=(db, ))
            thr_top_truants = threading.Thread(target=top_truants, args=(db, ))
            thr_top_subjects = threading.Thread(target=top_subjects, args=(db, ))
            thr_top_students.start()
            thr_top_truants.start()
            thr_top_subjects.start()

            start(DB_LIST_STUDENTS)

        # Добавление предмета.
        elif arg == DB_ADD_SUBJECT:
            thr_top_students.join()
            thr_top_truants.join()
            thr_top_subjects.join()

            print_subjects(db)
            add_subject(input('\nВведите название предмета: '), db)
            clear()

            # Обновление данных о рейтингах.
            thr_top_students = threading.Thread(target=top_students, args=(db, ))
            thr_top_truants = threading.Thread(target=top_truants, args=(db, ))
            thr_top_subjects = threading.Thread(target=top_subjects, args=(db, ))
            thr_top_students.start()
            thr_top_truants.start()
            thr_top_subjects.start()

            start(DB_LIST_SUBJECTS)

        # Добавление оценки.
        elif arg == DB_ADD_GRADE:
            thr_top_students.join()
            thr_top_truants.join()
            thr_top_subjects.join()

            print_students(db)
            print_subjects(db)

            student = input('\nИмя студента: ')
            subject = input('Название предмета: ')
            grade = input('Оценка по предмету: ')

            add_grade(student, subject, grade, datetime.now().date(), db)

            # Обновление данных о рейтинге.
            thr_top_students = threading.Thread(target=top_students, args=(db, ))
            thr_top_truants = threading.Thread(target=top_truants, args=(db, ))
            thr_top_subjects = threading.Thread(target=top_subjects, args=(db, ))
            thr_top_students.start()
            thr_top_truants.start()
            thr_top_subjects.start()

            clear()
            print_db(db)

        # Вывод списка студентов.
        elif arg == DB_LIST_STUDENTS:
            print_students(db)

        # Вывод списка предметов.
        elif arg == DB_LIST_SUBJECTS:
            print_subjects(db)

        # Вывод топ 10 студентов.
        elif arg == DB_TOP_10_STUDENTS:
            thr_top_students.join()
            print_top_students(db)

        # Вывод топ 10 прогульщиков
        elif arg == DB_TOP_10_TRUANTS:
            thr_top_truants.join()
            print_top_truants(db)

        # Вывод топ 10 по сложности учебных предметов.
        elif arg == DB_TOP_10_SUBJECTS:
            thr_top_subjects.join()
            print_top_subjects(db)

        # Сохранение изменений.
        elif arg == DB_SAVE_ALL:
            save_to_json(db)
            clear()
            print('База данных сохранена!\n')

        # Создание пустой бд.
        elif arg == DB_NEW_DB:
            thr_top_students.join()
            thr_top_truants.join()
            thr_top_subjects.join()

            db = create_empty_db()

            # Обновление данных о рейтинге.
            thr_top_students = threading.Thread(target=top_students, args=(db, ))
            thr_top_truants = threading.Thread(target=top_truants, args=(db, ))
            thr_top_subjects = threading.Thread(target=top_subjects, args=(db, ))

            thr_top_students.start()
            thr_top_truants.start()
            thr_top_subjects.start()

        # Выход из программы
        elif arg == DB_EXIT_PROGRAM:
            thr_top_students.join()
            thr_top_truants.join()
            thr_top_subjects.join()

            sys.exit()

    # Вывод списка действий.
    print('\n-----------\n')
    print('  1. Содержание')
    print('  2. Добавление студента')
    print('  3. Добавление предмета')
    print('  4. Добавление оценки по предмету')
    print('  5. Список студентов')
    print('  6. Список предметов')
    print('  7. Топ 10 студентов [по успеваемости]')
    print('  8. Топ 10 студентов [по прогулам]')
    print('  9. Топ 10 самых трудных предметов')
    print('  10. Сохранить изменения')
    print('  11. Создать пустую базу данных')
    print('  12. Выход')
    print('\n-----------\n')

    # Выбор пользователя.
    command = int(input('Выбор: '))

    # Очистка консоли.
    clear()

    # Рекурсивный вызов.
    start(command)
