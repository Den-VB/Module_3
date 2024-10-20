# Задача "Распаковка"
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = 3, a = "2 cтроки")
print_params(3, "2 cтроки")
print_params(c=[1, 2, 3])

values_list=["слово", True, 10]
values_dict={'a' : "3 cтроки", 'b' : False, 'c' : 3, }

print_params(*values_list)
print_params(**values_dict)

values_list_2=["слово", True]
print_params(*values_list_2, 42)
