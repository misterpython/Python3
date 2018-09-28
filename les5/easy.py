
import os
import shutil

def creation_dirs(name):

#Создает каталог(и) в текущей директории.
    
    os.makedirs(name)

    print('Папка(и) успешно создана(ы):', os.getcwd(), "\\", name)

    print('Каталоги и подкаталоги текущей директории:')
                
    for root, dirs, files in os.walk('.'):

        for _dir in dirs:

            print(_dir)

#creation_dirs('dir_23\dir_24')





import shutil

def delet_dirs(name):

#Удаляет каталог(и) в текущей директории.    

     
    shutil.rmtree(name)
        
    print('Удален  каталог(и):', name)

    print('Каталоги и подкаталоги текущей директории:')

    for root, dirs, files in os.walk('.'):

        for _dir in dirs:

            print(_dir)

#delet_dirs('dir_21')



def change_folder(name_dir):

    os.chdir(name_dir)

    print('Успешно перешли в директорию:', os.getcwd())


#change_folder('D:\Python\Python3\les5')


    

def lst_dir(path_):
    
#Функция выводит содержание директории в колонку.
    
    p = os.listdir(path_)
    
    for i in p:
        
        print(i)
        
#print(lst_dir('.'))









            
