# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
#from pathlib import Path

p = os.path.abspath("les5_3_easy.py")

#p = Path("les5_3_easy.py").resolve()

print(p)

dirnam, flnam = os.path.split(str(p))

cont_ = open(flnam).read()

open(os.path.join(dirnam, flnam),'w').write(cont_)
 
    


