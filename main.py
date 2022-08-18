

import os
from pickle import FALSE
import random
from time import sleep

#nSort = 3
#vermelhos = 0
#pretos = 0
#branco = 0 

random.seed(a=None, version=2)
rodadaSB = 1
saldo = 100
gasto = 0
aposta = 0.01
lucro: (aposta*14) - gasto
maiorSaldo = 0

#CALCULA VALOR DA APOSTA DE ACORDO COM A RODADA SEM VIR O BRANCO
def calcAposta():
    global rodadaSB

    if rodadaSB <= 9:
        return 0.01
    elif rodadaSB <= 15:
        return 0.02
    elif rodadaSB <= 19:
        return 0.03
    elif rodadaSB <= 21:
        return 0.04
    elif rodadaSB <= 24:
        return 0.05
    elif rodadaSB <= 26:
        return 0.06
    elif rodadaSB <= 28:
        return 0.07
    elif rodadaSB <= 29:
        return 0.08
    elif rodadaSB <= 30:
        return 0.09
    elif rodadaSB <= 32:
        return 0.10
    elif rodadaSB <= 33:
        return 0.11
    elif rodadaSB <= 34:
        return 0.12
    elif rodadaSB <= 35:
        return 0.13
    elif rodadaSB <= 36:
        return 0.14
    elif rodadaSB <= 37:
        return 0.15
    elif rodadaSB <= 38:
        return 0.17
    elif rodadaSB <= 39:
        return 0.18
    elif rodadaSB <= 40:
        return 0.20
    elif rodadaSB <= 41:
        return 0.21
    elif rodadaSB <= 42:
        return 0.23
    elif rodadaSB <= 43:
        return 0.25
    elif rodadaSB <= 44:
        return 0.27
    elif rodadaSB <= 45:
        return 0.29
    elif rodadaSB <= 46:
        return 0.31
    elif rodadaSB <= 47:
        return 0.34
    elif rodadaSB <= 48:
        return 0.37
    elif rodadaSB <= 49:
        return 0.40
    elif rodadaSB <= 50:
        return 0.43
    elif rodadaSB <= 51:
        return 0.46
    elif rodadaSB <= 52:
        return 0.50
    elif rodadaSB <= 53:
        return 0.54
    elif rodadaSB <= 54:
        return 0.59
    elif rodadaSB <= 55:
        return 0.63
    elif rodadaSB <= 56:
        return 0.68
    elif rodadaSB <= 57:
        return 0.74
    elif rodadaSB <= 58:
        return 0.80
    elif rodadaSB <= 59:
        return 0.86
    elif rodadaSB <= 60:
        return 0.93
    elif rodadaSB <= 61:
        return 1.01
    elif rodadaSB <= 62:
        return 1.09
    elif rodadaSB <= 63:
        return 1.18
    elif rodadaSB <= 64:
        return 1.27
    elif rodadaSB <= 65:
        return 1.37
    elif rodadaSB <= 66:
        return 1.48
    elif rodadaSB <= 67:
        return 1.60
    elif rodadaSB <= 68:
        return 1.73
    elif rodadaSB <= 69:
        return 1.87
    elif rodadaSB <= 70:
        return 2.02
    elif rodadaSB <= 71:
        return 2.18
    elif rodadaSB <= 72:
        return 2.36
    elif rodadaSB <= 73:
        return 2.54
    elif rodadaSB <= 74:
        return 2.75
    elif rodadaSB <= 75:
        return 2.97
    elif rodadaSB <= 76:
        return 3.21
    elif rodadaSB <= 77:
        return 3.46
    elif rodadaSB <= 78:
        return 3.74
    elif rodadaSB <= 79:
        return 4.04
    elif rodadaSB <= 80:
        return 4.36
    elif rodadaSB <= 81:
        return 4.71
    elif rodadaSB <= 82:
        return 5.09
    elif rodadaSB <= 83:
        return 5.5
    elif rodadaSB <= 84:
        return 5.94
    elif rodadaSB <= 85:
        return 6.42
    elif rodadaSB <= 86:
        return 6.93
    elif rodadaSB <= 87:
        return 7.48
    elif rodadaSB <= 88:
        return 8.08
    elif rodadaSB <= 89:
        return 8.73
    elif rodadaSB <= 90:
        return 9.43
    elif rodadaSB <= 91:
        return 10.18
    elif rodadaSB <= 92:
        return 11.00
    elif rodadaSB <= 93:
        return 12.83
    elif rodadaSB <= 94:
        return 12.83
    elif rodadaSB <= 95:
        return 13.86
    elif rodadaSB <= 96:
        return 14.97
    elif rodadaSB <= 97:
        return 16.17
    elif rodadaSB <= 98:
        return 17.46
    elif rodadaSB <= 99:
        return 18.86
    elif rodadaSB <= 100:
        return 20.37

def logaNum(rodada, numSort):
    global rodadaSB

    arquivo = open ( "teste.txt", "a")
    arquivo.write(f'Rodada: {rodada}   SB: {rodadaSB}   N:{numSort}\n')
    arquivo.close()

def calcBranco(res):
    global rodadaSB, saldo, gasto, aposta, maiorSaldo

    if res:
        saldo = saldo+(aposta*14)
        aposta = 0.01
        gasto = 0.01 #pq ja vou apostar no branco denovo
        rodadaSB=1
    else:
        rodadaSB=rodadaSB+1
        aposta = calcAposta()
        gasto = gasto + aposta
        saldo = saldo - aposta

    if saldo >= maiorSaldo:
        maiorSaldo = saldo


def proximoNum():
    global rodadaSB, saldo, gasto, aposta, maiorSaldo

    nSort = 3
    vermelhos = 0
    pretos = 0
    branco = 0

    while nSort:

        print(f'Rodadas branco: {rodadaSB} | Saldo: {saldo} | Aposta atual: {aposta} | Gasto atual: {gasto} | Lucro: {(aposta*14) - gasto} | maiorSaldo: {maiorSaldo}' ) 
        print(f'Preto: {pretos} | Vermelho: {vermelhos} | Branco: {branco} | TOTAL: {pretos+branco+vermelhos}' ) 
        nSort = random.randint(1, 1000000)
        
        nSort = (nSort%15) + 1
        #nSort = nSort+1
            
        print(f'GIROU : {nSort}' )  
        #print(nSort)  
       
        logaNum(pretos+branco+vermelhos, nSort)
        if nSort <= 7:
            vermelhos = vermelhos+1
            calcBranco(False)
        elif nSort <= 14:
            pretos = pretos+1
            calcBranco(False)
        else:   
            branco = branco+1
            calcBranco(True)
    
        if pretos+branco+vermelhos >= 3000:
            return
        #gc.collect(generation=2)
        #sleep(0.5)
        os.system('cls')

if __name__ == '__main__':
    print('Iniciando roleta')
    sleep(1)
    proximoNum()

    print ('fim')

   




