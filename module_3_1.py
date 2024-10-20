# Задача "Счётчик вызовов"
calls = 0

def count_calls():
    global calls
    print("Количество вызовов строковых функций: ", calls)

def string_info():
    global calls
    string = input("Введите слово: ")
    string_info = ((len(string)), string.lower(), string.upper())
    print("Длина слова: ", string_info)
    calls = calls + 1

def is_contains():
    global calls
    string = input("Введите слово: ")
    string = string.lower()
    to_search = input("Введите список слов для поиска через пробел: ")
    to_search = to_search.lower()
    contains = to_search.split()
    found = string in contains
    print(found)
    calls = calls + 1

string_info()
is_contains()
string_info()
is_contains()
count_calls()