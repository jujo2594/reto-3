import os 
import campus
import trainers
import incidencia

if __name__ == '__main__':
    iniciar = True
    while iniciar:
        os.system('clear') and os.system('cls')
        print('MENU PRINCIPAL')
        print('1. Gestion de campus', '2. Gestion de trainers', '3. Gestion de incidencias', '4. Salir del programa', sep = '\n')
        opcion = int(input('Ingrese la operacion del menu que desea realizar:'))
        try:
            if opcion == 1:
                os.system('cls') and os.system('clear')
                campus.loadInfoCampus('campus.json')
                campus.mainMenu()
            elif opcion == 2:
                os.system('cls') and os.system('clear')
                trainers.loadInfoTrainer('trainers.json')
                trainers.mainMenu()
            elif opcion == 3:
                os.system('cls') and os.system('clear')
                incidencia.loadInfoIncidencias('incidencia.json')
                incidencia.mainMenu()
            elif opcion == 4:
                iniciar = False
            else:
                print('La opcion ingresada no se encuentra en el menu principal')
        except Exception as e:
            print(f'Error: {e}')
            os.system('pause') and os.system('sleep 5')