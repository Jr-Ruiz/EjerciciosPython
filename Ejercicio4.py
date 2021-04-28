#!/usr/bin/python
# encoding: utf-8
#Utilización: invocar al programa introduciendo un año como argumento a la llamada. Es decir: python3 Ejercicio4.py 2021
#Esta llamada devolverá False

import sys

def es_bisiesto(anyo):
        if anyo%400==0:
                return True
        elif anyo%100==0:
                return False
        elif anyo%4==0:
                return True
        else:
                return False

print(es_bisiesto(int(sys.argv[1])))
