#!/usr/bin/python
#encoding: utf-8

import sys

cadena=sys.argv[1]
contador=0

for i in range(0,len(cadena)//2):
	if cadena[i]==cadena[-i-1]:
		contador+=1

if contador==(len(cadena)//2):
	print("Palíndromo")
else:
	print("No palíndromo")
