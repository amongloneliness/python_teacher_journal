# Модуль для работы с json.
import json


# Загрузка БД из json.
def load_from_json(json_file):
    with open(json_file, 'r') as json_filename:
        return json.loads(json_filename.read())
