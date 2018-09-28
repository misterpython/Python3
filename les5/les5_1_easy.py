# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

# Создание дерева директорий в текущем каталоге.

print('Текущия директория:', os.getcwd())

mkd = input('Создать дерево каталогов dir_1 - dir_9 в текущей директории(y/n):')

if mkd == 'y':
    try:
        os.makedirs('dir_1/dir_2/dir_3/dir_4/dir_5/dir_6/dir_7/dir_8/dir_9')
    except:
        input('Каталоги уже существуют!')
        
    print('Создано дерево каталогов dir_1 - dir_9')
            
    print('Список содержимого текущей директории c новыми папками:')  

    for root, dirs, files in os.walk('.'):

        for _dir in dirs:

            print(_dir)



       

import shutil

#Удаление дерева директорий в текущем каталоге.

print('Текущия директория:', os.getcwd())

mkd = input('Удалить дерево каталогов dir_1 - dir_9 в текущей директории(y/n):')

if mkd == 'y':
    try:
        shutil.rmtree('dir_1')
    except:
        input('Каталогов не существует!')

    print('Дерева каталогов dir_1 - dir_9 успешно удалено.')

    print('Список содержимого текущей директории после удаления:')
        
    for root, dirs, files in os.walk('.'):

        for _dir in dirs:

            print(_dir)



    
