from os import system, name


# Очистка командной строки.
def clear():

    # Для windows.
    if name == 'nt':
        _ = system('cls')
    # Для mac и linux.
    else:
        _ = system('clear')

    return
