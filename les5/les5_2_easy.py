# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


import os

print(os.getcwd())
    
for root, dirs, files in os.walk('.'):

    for _dir in dirs:

        print(_dir)
 
    
