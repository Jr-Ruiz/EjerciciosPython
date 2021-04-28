#!/usr/bin/python
#encoding: utf-8
#La llamada al programa requiere como argumento la introducción del número de 'tiradas' que se van a realizar
#
#Por ejemplo: python3 Ejercicio5.py 100000
#La llamada anterior hará 100000 tiradas entre las cuatro opciones ('a','b','c' o 'd')

import sys
from random import choice
tirada=0
fin=float(sys.argv[1])
a=b=c=d=0
while tirada <= fin:
    	resultado=choice(['a','b','c','d'])
    	if resultado == "a":
            	a+=1 #Equivalente a a=a+1
    	elif resultado  == "b":
            	b+=1
    	elif resultado =="c":
            	c+=1
    	else:
            	d+=1
    	tirada=tirada+1

print("'a' ha salido el "+ str("{:.3f}".format(a/fin)) +"% de las veces")
print("'b' ha salido el "+ str("{:.3f}".format(b/fin)) +"% de las veces")
print("'c' ha salido el "+ str("{:.3f}".format(c/fin)) +"% de las veces")
print("'d' ha salido el "+ str("{:.3f}".format(d/fin)) +"% de las veces")

#"{:.3f}".format() muestra el número dentro de format() con tres decimales
