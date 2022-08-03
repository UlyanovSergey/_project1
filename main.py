
""" Модуль верхнего уровня, для учебного проекта 1: Крестики-нолики """
# импорт дополнительных модулей
import help


from pathlib import Path
from sys import argv
from configparser import ConfigParser as CP




# ИСПОЛЬЗОВАТЬ: в этой переменной должен храниться путь к файлу players.ini - посмотрите в моём коде, как его получить корректным образом
# сохраняет путь к файлу в переменную (получилось только с абсолютным путем)
SCRIPT_DIR = Path('C:/Users/ulyanovs/PycharmProjects/_project1')
PLAYERS_INI_PATH = SCRIPT_DIR / 'players.ini'



# глобальные переменные
STATS = {}


# суперцикл
while True:
    command = input(' Для начала игры введите new для завершения exit: ').lower()

    if command in ('quit', 'exit', 'q', 'e'):
        break

    elif command in ('new', 'n'):

        # ИСПОЛЬЗОВАТЬ: 1. не стоит размещать код объявления функции непосредственно рядом с вызовом функции - это не позволяет ясно увидеть логику выполнения программы; внимательно изучите примеры расположения кода, которые я демонстрирую в своём проекте
        #               2. почему не используете сигнатуры функций из документа Архитектура?
        # ИСПРАВИТЬ: поместите код объявления функции в нужный модуль
        def read_ini():
            """ Читает данные из файла """
            # читает из файла player.ini
            with PLAYERS_INI_PATH.open() as ini_file:
                # для проверки работы функции
                print(f"P{ini_file.read()}")

            # ИСПРАВИТЬ: 1. не вижу такой глобальной переменной - где она? и если собираетесь изменять глобальную переменную из локального пространства имён, то должны в начале тела функции заявить об этом с помощью ключевого слова global
            #            2. вы сохранили в переменную объект str - это то, что возвращает метод read() - но эта строка должна быть проанализирована и преобразована в нужную нам структуру данных - зря мы их разрабатывали и прописывали разве?






        # начало партии
        # ИСПРАВИТЬ: поместите код объявления функции в нужный модуль
        def show_field():
            """ Выводит в стандартный поток игровое поле с ходами игроков """


        # ИСПРАВИТЬ: поместите код объявления функции в нужный модуль
        def check_win():
            """ Проверяет игровое поле, есть ли выигрышная комбинация """
            pass

    read_ini()
# Пример вывода игрового поля

#  X | O |
# ———————————
#  O | X | X
# ———————————
#    |   |

# вызов функций

