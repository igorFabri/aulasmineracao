# -*- coding: utf-8 -*-
"""
Created on Fri May  4 17:27:01 2018

@author: ice
"""

import sys
sys.path.insert(0, '/ice/Downloads/apyori/apyori-master')

from apyori import apriori

file = open("file.txt","r")

transacoes = []

for reg in file:
    if(";" in reg):
        continue
    beer,nuts,cheese,jam,butter = reg.split(",")
    
    registro = []    
    
    if(beer == "1"):
        registro.append("beer")
    if(nuts == "1"):
        registro.append("nuts")
    if(cheese == "1"):
        registro.append("cheese")
    if(jam == "1"):
        registro.append("jam")
    if(butter == "1"):
        registro.append("butter")
        
    transacoes.append(registro)
    
print(transacoes)