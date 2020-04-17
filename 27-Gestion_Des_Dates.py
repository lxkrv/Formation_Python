#coding:utf-8
import os
import time #--->objet du cours
# for windows
os.system('cls')
#os.system("ls")

import datetime

date1 = datetime.datetime(2018, 2, 12, 9, 36, 42)
date2 = datetime.datetime(2018, 2, 27, 9, 36, 42)
print(date1,"\n",date2)

if date1 < date2:
    print("date1 est plus ancien que date2")
else:
    print("date1 est plus récente que date2")

date3 = datetime.date(2018, 2, 12)
date4 = datetime.date(2018, 2, 27)
print(date3,"\n",date4)

print("le type de date3 est : ", type(date3))
print("uniquement la date ",date3.year)
print("")
t1 = datetime.time(23,00,46)
print(t1)
print("")

from datetime import date
now = date.today()
print(now)

import datetime
from datetime import date
now = date.today()
born = datetime.date(1977, 4, 17)
print(f"{now.year - born.year} ans.")