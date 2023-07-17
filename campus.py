import os
import core
import random
diccCampus = { }
area = {}
salones = {}
equipos = {}
def  loadInfoCampus(fileName):
    global diccCampus
    if (core.checkFile('campus.json')):
        diccCampus = core.loadInfo('campus.json')
    else: 
        core.crearFile('campus.json', diccCampus)
        
def mainMenu():
    os.system('cls') and os.system('clear')
    iniciarCampus = True        
    print('MENU CONTROL CAMPUS')
    print('1. Ingreso de area', '2. Ingreso de Salon', '3. Ingreso Equipos', '4. Volver al menu principal', sep='\n')
    opcion = int(input('Ingrese la opcion del menu que desea realizar:'))
    
    if opcion == 1:
        idArea = (str(random.randint(1,10000))).zfill(5)
        nombreArea = (input('Ingrese el area de campus: ').strip()).upper()
        
        zonas = {
            'idArea':idArea,
            # 'nombreArea': nombreArea
        }
        isNombreRepetido = False
        for item in area:
            checkNombre = area[item].get('nombreArea',-1)
            if checkNombre == nombreArea:
                isNombreRepetido = True
                break
        if not isNombreRepetido:
            zonas.update({'nombreArea':nombreArea})
            area.update({f'{idArea}':zonas})
            diccCampus.update({'areas':area})
        else:
            print('Ingrese otro nombre de area diferente')
            
        # checkArea = area.get('idArea',-1)
        # if checkArea == -1:
        #     area.update({f'{idArea}':zonas})
        #     diccCampus.update({'areas':area})
        # else:
        #     print('Ingrese una zona diferente')
        print(area)
        print(diccCampus)
        core.crearFile('campus.json',diccCampus)
        os.system('pause') and os.system('sleep 5')
        
    elif opcion == 2:
        idSalon = (str(random.randint(1,10000))).zfill(5)
        nombreSalon = (input('Ingrese el nombre del salon: ').strip()).upper()
        
        salon = {
                'idSalon':idSalon
        }
        
        isNombreSalon = False
        for item in salones:
            checkSalon = salones[item].get('nombreSalon',-1)
            if checkSalon == nombreSalon:
                isNombreSalon = True
                break
        if not isNombreSalon:
            salon.update({'nombreSalon':nombreSalon})
            salones.update({f'{idSalon}':salon})
            diccCampus.update({'salones':salones})
        else:
            print('El nombre del salon ya se encuentra ingresado.')
        core.crearFile('campus.json',diccCampus)
        
    elif opcion == 3:
        idEquipo = (str(random.randint(1,10000))).zfill(5)
        cantEquipos = int(input('Ingrese la cantidad de equipos dentro de un salon: '))
        hardware = ['TECLADO', 'MONITOR', 'MOUSE', 'CPU', 'DIADEMA']
        equipo = {
            'idEquipo': idEquipo,
            'cantEquipos': cantEquipos,
            'hardware': hardware
        }
        equipos.update({f'{idEquipo}':equipo})
        diccCampus.update({'equipos':equipos})
        core.crearFile('campus.json',diccCampus)
    elif opcion == 4:
        iniciarCampus = False
    if iniciarCampus:
            mainMenu()    