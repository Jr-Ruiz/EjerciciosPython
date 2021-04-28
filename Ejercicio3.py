#!/usr/bin/python
# encoding: utf-8

import random	#librería con las funciones para 'desordenar' listas al azar

palos=['C','T','D','P'] #generamos los 4 palos de la baraja francesa
numeros=['As',2,3,4,5,6,7,8,9,10,'J','Q','K'] # generamos los números de las cartas de cada palo

#inicializamos variables, indicando que repartiremos 5 cartas
#y que jugaremos con 2 jokers

baraja=[]
cartas=5
numero_jokers=2
jugador1=[]
jugador2=[]


def is_poker(mano):
	"""Función para comprobar, en primer lugar cuántos comodines tenemos
	y en segundo lugar cuántas cartas repetidas hay en la mano, buscando
	secuencialmente desde 'As' hasta 'K'. Si se encuentran más de 3 figuras
	del mismo valor o la suma de las cartas del mismo valor y los comodines
	es superior a 3 se deja de buscar y se muestra el Póker por pantalla"""

	joker=0

	for j in range(0,len(mano)):
		if 'Jk' in mano[j]:
			joker+=1

	for i in numeros:
		poker=joker

		for j in range(0,len(mano)):
			if i in mano[j]:
				poker+=1
		if poker>3:
			print("\n POKER de "+str(i)+"\n")
			return True
			break

def genera_baraja():
	"""Con esta función generamos las 52 cartas correspondientes
	a las 13 cartas de cada palo y añadimos el número de comodines
	indicados al principio"""

	for i in palos:
		contador=0
		while contador<len(numeros):
			baraja.append((i,numeros[contador]))
			contador+=1

	for i in range(0,numero_jokers):
		baraja.append((' ','Jk'))

	#Mostramos la baraja para comprobar que todo ha ido bien
	print(baraja)
	print(len(baraja))

	#Desordenamos la baraja
	random.shuffle(baraja)


def repartir_cartas():
	"""Vamos extrayendo del final de la baraja desordenada
	el número de cartas indicado más arriba y las añadimos
	a cada jugador"""

	for i in range(0,cartas):
		jugador1.append(baraja.pop())
		jugador2.append(baraja.pop())

	print(jugador1)
	print(jugador2) #Mostramos las barajas para hacer comprobaciones


genera_baraja()
repartir_cartas()
is_poker(jugador1)
is_poker(jugador2)
