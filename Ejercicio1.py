#!/usr/bin/python
# encoding: utf-8

def introduce():
        parar=0
        matricula=[]
        while parar == 0:
                modulo=raw_input("Introduce un modulo\n")
                if modulo:
                        matricula.append(modulo)
                else:
                        parar=1
        muestra(matricula)

def muestra(listado):
        for elemento in listado:
                print elemento

introduce()
