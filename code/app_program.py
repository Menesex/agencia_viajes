ls_viajeros = []
import os
viajero = ''
def fnt_limpiar():
    os.system('cls')
    print('Autor: Menesex ✍(◔◡◔)\ncopyright© 2024\nUniversidad católica luis amigó 🏢')
    print('.............................................................................\n\n')
def fnt_agente(op):
    global sw, viajero
    if op == '0':
        sw = False
    elif op == '1':
        fnt_limpiar()
        print ('<<< Agregar viajero >>>')
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        if int(edad) > 0  and int(edad) <= 25:
            viajero = nombre+' '+apellido+' | '+edad+' años'
            ls_viajeros.append(viajero)
            print("\n¡Viajero registrado correctamente!")
            input('Presione <ENTER> para continuar..')
        else:
            input('ERROR: Edad fuera de rango <ENTER>...')
    elif op == '2':
        fnt_limpiar()
        if len(ls_viajeros) > 0:
            print('<<< 📃LISTA DE VIAJEROS📃 >>>')
            print(f'Lista: {ls_viajeros}')
            input('Fin de la consulta <ENTER>...')
        else:
            input('No hay datos de viajeros para mostrar <ENTER>...')
        
sw = True
while sw == True:
    fnt_limpiar()
    opcion = input('<<< [💠] MENU PRINCIPAL [💠] >>>\n\n[0]Salir\n[1]Agregar\n[2]Mostrar\n▶ ')
    fnt_agente(opcion)
