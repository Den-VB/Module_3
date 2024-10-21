# Задача "Рекурсивное умножение цифр"
def get_multiplied_digits(number):
    str_number = str(int(number))
    first=int(str_number[0])
    if first == 0:
        first=1
    if len(str_number)>1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


number = int(input("введите число: "))
print(get_multiplied_digits(number))