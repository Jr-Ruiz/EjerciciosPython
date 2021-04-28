#!/usr/bin/python
#encoding: utf-8

from random import choice

operacion=input("""Introduce la operación con la que quieres entrenarte
    1. Sumas
    2. Restas
    3. Multiplicaciones
    """)

rango=int(input("Introduce el número más grande con el que quieres jugar\n"))
aciertos=0

seguir="S"
while seguir=="S":
    print("Llevas "+str(aciertos)+" aciertos\n")
    numero_1 = choice(range(0, rango))
    numero_2 = choice(range(0, rango))

    if operacion == "1":
        op = "+"
        correcto = numero_1 + numero_2
    elif operacion == "2":
        op = "-"
        correcto = numero_1 - numero_2
    else:
        op = "*"
        correcto = numero_1 * numero_2

    try:
        resultado=int(input("¿Cuánto es "+str(numero_1)+op+str(numero_2)+"?\n"))
        if resultado == correcto:
            seguir = input("Correcto. ¿Quieres probar otra vez?[S/N]")
            aciertos += 1
        else:
            print(input("El resultado no es válido. Pulsa cualquier tecla para seguir"))
    except ValueError:
        print(input("El resultado no es un número. Pulsa [Intro] para continuar"))
