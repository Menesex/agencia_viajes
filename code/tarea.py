'''
elaborar un programa que permita calcular el área de un lote y luego determine su valor de acuerdo a las sig condiciones


PEDIR MEDIDAS (en metros)
Frente:
Fondo:
m2 = FrentexFondo

1.Urbano 
    M2 = 25.000
    Permiso Construccion = 0.45
2.Comercial
    M2 = 60.000
    Permiso Construccion = 0.75
3.Campestre
    M2 = 35.000
    Permiso Construccion = 0.15
    
FUNCIONES
[1]Agregar un nuevo lote
[2]Mostrar lotes
    a. Urbanos
    b. Comercial
    c. Campestre
'''
import os

def fnt_limpiar():
    os.system('cls')

def fnt_selector(op):
    global sw
    if op == '0':
        sw = False
    elif op == '1':
        fnt_agregar()
    elif op == '2':
        fnt_consultar()
sw = True
while sw == True:
    fnt_limpiar()
    op = input('CALCULADOR DE ÁREA\n[0]Salir\n[1]Agregar un nuevo lote\n[2]Mostrar lotes\n')
    fnt_selector(op)