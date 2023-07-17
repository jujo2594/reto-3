import os
import core
import random
import datetime

diccIncidencias = {}

def loadInfoIncidencias(fileName):
    global diccIncidencias
    if core.checkFile('incidencia.json'):
        diccIncidencias = core.loadInfo('incidencia.json')
    else:
        core.crearFile('incidencia.json',diccIncidencias)

iniciarIncidencia = True        
def mainMenu():
    os.system('cls') and os.system('clear')
    print('MENU INCIDENCIAS')
    print('1. Ingresar Incidencia', '2. Volver al menu inicial', sep ='\n')
    opcion = int(input('Ingrese la opcion que desea realizar: '))
    if opcion == 1:
        idIncidente = (str(random.randint(1,10000))).zfill(5)
        tipoIncidente = (input('Ingrese el tipo de incidente: ').strip()).upper()
        descripcion = (input('Ingrese descripcion de incidente: ').strip()).upper()
        fecha = datetime.datetime.now()
        fechaFinal = fecha.strftime("%d/%m/%Y")
        categoria = (input('Ingrese la categoria del incidente: ').strip()).upper()
        while((categoria != 'HARDWARE') and (categoria != 'SOFTWARE')):
            categoria = (input('Ingrese la categoria del incidente: ').strip()).upper()
        diccCampus = core.loadInfo('campus.json')
        for item in diccCampus['areas']:
            print(f'AREA: {diccCampus["areas"][item]["nombreArea"]}')
        areaIncidencia = (input('Ingrese el area donde se desarrollo la incidencia: ').strip()).upper()
        checkArea = False
        for item in diccCampus['areas']:
            if diccCampus['areas'][item]['nombreArea'] == areaIncidencia:
                checkArea = True
                break
        while not checkArea:
            areaIncidencia = (input('Ingrese el area donde se desarrollo la incidencia: ').strip()).upper()
            
        for item in diccCampus['salones']:
            print(f'SALON: {diccCampus["salones"][item]["nombreSalon"]}')
        salonIncidencia = (input('Ingrese el salon donde se desarrollo la incidencia: ').strip()).upper()
        checkSalon = False
        for item in diccCampus['areas']:
            if diccCampus['areas'][item]['nombreArea'] == areaIncidencia:
                checkSalon = True
                break
        while not checkSalon:
            areaIncidencia = (input('Ingrese el area donde se desarrollo la incidencia: ').strip()).upper()
        incidencia = {
            'idIncidente':idIncidente,
            'tipoIncidente': tipoIncidente,
            'descripcion': descripcion,
            'fecha': fechaFinal,
            'categoria':categoria,
            'areaIncidencia': areaIncidencia,
            'salonIncidencia': salonIncidencia
        }
        diccIncidencias.update({f'{idIncidente}':incidencia})
        core.crearFile('incidencia.json',diccIncidencias)
        os.system('pause') and os.system('sleep 5')
    elif opcion == 2:
        iniciarIncidencia = False
        if iniciarIncidencia:
            mainMenu()
    else:
        print('Ingrese una opcion que se encuentra dentro del menu')