# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    
#Функция в качестве аргументов принимает n - начальный элемент последовательности Фибоначчи,
#m - конечный элемент последовательности и возвращает в виде списка ряд с n по m.   

    lst = []
    
    for i in range(n, m + 1):
                      
        form_binet = 1.618034 ** i / 2.236068

        sequence = round(form_binet)
        
        lst.append(sequence)
        
    return lst 



lst = fibonacci(1, 10) #Вызов функции.

print(lst)
