# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter_lightweight(a, b):

#Функция в качестве аргументов принимает: a - значение возвращаемое
#другой функцией (True или False), в качестве второго аргумента b - список.    
#При True итерирует значения из списка b - больше нуля.
#При False итерирует значение из списка b - меньше нуля.
#При значении None вместо аргумента a - итерируется все элементы списка,
#кроме пустой строки.     

    lst = []
    
    if a == True:
        
        [lst.append(i) for i in b if i > 0]

    if a == False:
        
        [lst.append(i) for i in b if i < 0]
        
    if a == None:
        
        [lst.append(i) for i in b if i != ""]
             
    return lst   



def func(x):
    if x > 0:
        return 1
    else:
        return 0       

x = 0
b = [1, -4, 0, 6, 0, 8, 0, -10]

c = filter_lightweight(None, [1, -4, 0, 6, 0, 8, 0, -10])
print(c)


