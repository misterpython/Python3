# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):

    ndigits_ = 10 ** ndigits

    number_ = int(number * ndigits_) / ndigits_

    _number = number - number_

    _ndigits = ndigits_ * 10

    resd = int(_number * _ndigits)

    if resd >= 5:
        result = 1/ndigits_ + number_
    
    if resd <= 4:
        result = number_
    return result

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))














    
    


