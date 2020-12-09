import csv
import re
from csv import reader
import itertools
import json
import numpy as np

lista = []
listareal = []
contador = 0
edad = 0
sueldo = 0


class info:
    def __init__(self, id, nombre, apellido,edad , puesto, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.puesto = puesto
        self.salario = salario


def opcion1():
    print("_______________________________________")
    print("| 1) INTRODUCIR RUTA DE ARCHIVO       |")
    print("| 2) REGRESAR AL MENU                 |")
    print("_______________________________________")
    try:
        opcion = int(input("Opcion:"))
    except:
        opcion1()

    if opcion == 1:
        global listareal
        global lista
        listaa = []

        ruta = input("Ingrese Ruta:")
        with open(ruta, 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            if header != None:
                listaa = list(csv_reader)

        print(listaa)



        listaa = np.unique(listaa, axis=0)

        print(listaa)

        if lista == []:
            for jk in listaa:
                if lista == []:
                    lista.append(info(jk[0], jk[1], jk[2], jk[3], jk[4], jk[5]))
                else:
                    lista.append(info(jk[0], jk[1], jk[2], jk[3], jk[4], jk[5]))

        for jk in lista:
            print("aqui"+jk.id, jk.nombre,jk.edad)


    # segunda parte

    #             listareal.append(info(comparacion.id,comparacion.nombre,comparacion.apellido,comparacion.puesto,comparacion.salario))

    elif opcion == 2:
        main()


def calculo():
    global edad
    global contador
    global sueldo
    for jk in lista:
        contador = contador + 1
        edad = edad + int(jk.edad)
        sueldo = sueldo + int(jk.salario)
    print("|Candidatos: " + str(contador) + "|", "Edad promedio: " + str(edad) + "|",
          "Salario Promedio: " + str(sueldo) + "|")


def archivo():
    global edad
    global contador
    global sueldo
    data = {}
    if contador != 0:
        edp = 0
        sup = 0
        edp = edad / contador
        sup = sueldo / contador
        data = {'Desarrollador': [{'Candidatos': contador, 'Edad Promedio': edp, 'Pretension Salarial': sup}]}
        with open(r"C:\Users\denni\OneDrive\Desktop\Calculos.txt", 'w') as outfile:
            json.dump(data, outfile)
            print("Archivo Creado Buscar en Escritorio : Calculos.txt ")
            contador = 0
            edad = 0
            sueldo = 0
    else:
        print("No se han hechos calculos")


def main():
    opcion = 0
    while (opcion != 4):
        print("  _______________________________________ ")
        print("|Dennis Alexnader Gamboa Stokes 201700747|")
        print("| _______________________________________|")
        print("|                                        |")
        print("| 1) LEER DATOS DE CVS                   |")
        print("| 2) CALCULAR DATOS                      |")
        print("| 3) CREAR ARCHIVO                       |")
        print("| >> ESCOGA OPCION                       |")
        print("| _______________________________________|")
        try:
            opcion = int(input("Opcion:"))
        except:
            main()

        if opcion == 1:  # CARGAR ARCHIVO
            print("")
            opcion1()

        elif opcion == 2:  # GRAFICAR ARCHIVO   <
            print("_______________________________________")
            calculo()

        elif opcion == 3:  # GRAFICAR ARCHIVO   <
            print("_______________________________________")
            archivo()
        else:
            print("Valor erroneo")
    # analizador("CARGAR archivo1, archivo_2, archivo3")


if __name__ == "__main__":
    main()