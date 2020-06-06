# -*- coding: utf-8 -*-
def suma(n1, n2):
    return n1 + n2
def resta(n1,n2):
    return n1 - n2
def multiplicacion(n1, n2):
    return n1*n2
def division(n1, n2):
    return n1/n2



print('BIENVENIDO A CALCULADORA BÁSICA')
print('comencemos')
opcion1 = input('introduce un valor numérico   ')
opcion2 = input('introduce un valor numérico   ')
print('escoge la operación')
operacion = input('1 SUMA, 2 RESTA, 3 MULTIPLICACION, 4 DIVISIÓN    ')
if operacion == 1:
    print(suma(opcion1, opcion2))
elif operacion == 2:
    print(resta(opcion1, opcion2))
elif operacion == 3:
    print(multiplicacion(opcion1, opcion2))
elif operacion == 4:
    print(division(opcion1, opcion2))
else:
    print('fin')
