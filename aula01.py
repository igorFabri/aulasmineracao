# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 16:17:12 2018

@author: Igor

Para executar parte do código, grifa-se parte do código e aperte shift+Enter.
"""

x = 11.1

print("Já já já ja vai !")

lista =  ['abc', 234,2.4,"asd",543.234]

print(lista[2])
print(lista[1:3])
print(lista[2:])
print(lista[:2])

inteiro = int("32")


print(9/2)

tupla =  ['abc', 234,2.4,"asd",543.234]
x = "234"

if x in tupla:
    print(str(x) + "está na tupla.")
elif("70.2" in tupla or 2.23 in tupla):
    print("2.23 esta na tupla")
else:
    print(str(x) +"não está na tupla.")
    
c = 0    
while (c < 9):
    print('Contagem ',c)
    c += 1
else:
    print("Not")

for t in tupla:
    print(t)    
    
print("End")

import time
import datetime

while True:
    for i in range(0,9):
        print("|                 %s                    " % (str(datetime.datetime.now())))
        
    time.sleep(3)
    print("\n")
        