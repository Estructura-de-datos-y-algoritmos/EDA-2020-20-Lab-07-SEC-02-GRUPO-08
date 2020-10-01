"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
from time import process_time
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


accidentsFile = 'US_Accidents_Dec19.csv'
#accidentsFile = 'prueba.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimento 1")
    print("4- Requerimento 2")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de crimenes ....")
        t1 = process_time()
        controller.loadData(cont, accidentsFile)
        print("Elementos cargados\n", lt.size(cont["accident"]))
        altura = controller.altura(cont["date"])
        datos = controller.indexSize(cont["date"])
        t2 = process_time()
        print("Altura del arbol\n", altura)
        print("Elmentos cargados\n", datos)
        t = t2-t1
        print("Tiempo requerido: ", t)

    elif int(inputs[0]) == 3:
        print("\nBuscando los accidentes de una fecha: ")
        
        fecha = input("Digite la fecha a buscar de la forma AAAA-MM-DD: ")
        lst = controller.accidentesFecha(cont, fecha)
        itera = it.newIterator(lst)
        while it.hasNext(itera):
            value = it.next(itera)
            print("Tipo de severidad :", value["severidad"], "Numero de accidentes: ", lt.size(value["lst_id"]))
        


    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 1 del reto 3: ")

    else:
        sys.exit(0)
sys.exit(0)
