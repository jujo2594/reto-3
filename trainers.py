import os
import core
import random

diccTrainers = {}

def loadInfoTrainer(fileName):
    global diccTrainers
    if core.checkFile('trainers.json'):
        diccTrainers = core.loadInfo('trainers.json')
    else:
        core.crearFile('trainers.json',diccTrainers)

iniciarTrainer = True
def mainMenu():
    os.system('cls') and os.system('clear')
    print('INGRESO DE TRAINERS')
    print('1. Registrar Trainer','2. Volver al menu principal: ', sep = '\n')
    opcion = int(input('Ingrese la opcion que desea ejecutar: '))
    if opcion == 1:
        idTrainer = (str(random.randint(1,10000))).zfill(5)
        nombreTrainer = (input('Ingrese el nombre del trainer: ').strip()).upper()
        emailPersonal = (input('Ingrese el email personal: ').strip()).upper()
        emailCorporativo = (input('Ingrese el email corporativo: ').strip()).upper()
        celularPersonal = int(input('Ingrese el celular personal: '))
        telefonoFijo = int(input('Ingrese el telefono fijo personal: '))
        telefonoCorporativo = int(input('Ingrese el telefono coporativo: '))
        celularEmpresarial = int(input('Ingrese el celular corporativo: '))
        
        trainer ={
            'idTrainer':idTrainer,
            'nombreTrainer':nombreTrainer,
            'emailPersonal':emailPersonal,
            'emailCorporativo':emailCorporativo,
            'celularPersonal':celularPersonal,
            'telefonoFijo': telefonoFijo,
            'telefonoCorporativo': telefonoCorporativo,
            'celularEmpresarial': celularEmpresarial
        }
        
        diccTrainers.update({f'{idTrainer}':trainer})
        core.crearFile('trainers.json',diccTrainers)
    elif opcion == 2:
        iniciarTrainer = False
        if iniciarTrainer:
            mainMenu()
