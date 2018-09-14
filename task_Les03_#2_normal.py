# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
 


def sort_to_max(origin_list):

#Функция в качестве аргумента 'origin_list' принимает список
#и возвращает отсортированный по возрастанию список.     

    i = 0

    temp_storg = []
    
    temp_storgt1 = []
    
    num_of_lst = len(origin_list)

    while i <= num_of_lst - 1:
    
        min_elmt_lst = min(origin_list)   #сортируем список в 'temp_storg'.  
    
        temp_storg.append(min_elmt_lst)
    
        origin_list.remove(min_elmt_lst)

        i += 1    
            
    origin_list = [i for i in temp_storg]  #загружаем отсортированный список в 'origin_list' 

    return origin_list    

    

a = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]) #Вызов функции.

print(a)















