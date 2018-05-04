# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:46:21 2018

@author: ice
"""
import sys
sys.path.insert(0, '/ice/Downloads/apyori/apyori-master')

from apyori import apriori

def printMaiorQueDois(resultado):
    for res in resultado :
        if(len(res.items) >= 2):
            print(res.items)

transacoes = [
    ['beer', 'nuts', 'cheese'],
    ['beer', 'nuts', 'jam'],
    ['beer', 'butter'],
    ['nuts', 'cheese'],
    ['beer', 'nuts', 'cheese', 'jam'],
    ['butter'],
    ['beer', 'nuts', 'jam', 'butter'],
    ['jam']
]

resultado = list(apriori(transacoes,min_support=0.5, min_confidence=0.8, min_lift=1.0))
            
printMaiorQueDois(resultado)

