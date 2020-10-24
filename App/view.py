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
#accidentsFile = 'us_accidents_dis_2016.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
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
        print("\nBuscando accidentes anteriores a una fecha: ")

        fecha = input("Digite la fecha a buscar de la forma AAAA-MM-DD: ")      #LE FALTA 
        rank = controller.A_antesFecha(cont, fecha)
        print("\nEl total de accidentes reportados antes de ", fecha, "son", rank)


    elif int(inputs[0]) == 5:
        print("\nBuscando accidentes en un rango de fechas: ")

        fecha1 = input("Digite el rango inferior a buscar de la forma AAAA-MM-DD: ")
        fecha2 = input("Digite el rango superior a buscar de la forma AAAA-MM-DD: ")
        
        accidente, server = controller.accidentesRango(cont, fecha1, fecha2)
        print("\nEl total de accidentes reportados entre ", fecha1, "y", fecha2, "son ", accidente)
        maximo_val = 0
        for k in server:
            if maximo_val < server[k]:
                maximo_val = server[k]
                categoriaa = k
        print("La categoria con más accidentes reportados es la ", categoriaa, "con ", maximo_val)

    
    elif int(inputs[0]) == 6:
        print("\nBuscando el estado con más accidentes: ")

        fecha1 = input("Digite el rango inferior a buscar de la forma AAAA-MM-DD: ")
        fecha2 = input("Digite el rango superior a buscar de la forma AAAA-MM-DD: ")

        accidente1, server2 = controller.accidentesRango1(cont, fecha1, fecha2)
        print("\nEl total de accidentes reportados entre ", fecha1, "y", fecha2, "son ", accidente1)
        maximo_val = 0
        for k in server2:
            if maximo_val < server2[k]:
                maximo_val = server2[k]
                estado = k
        print("El estado con más accidentes reportados es  ", estado, "con ", maximo_val)

    
    elif int(inputs[0]) == 7:
        print("\nConocer accidentes por rangos de horas: ")

        hora10 = input("Digite el rango inferior a buscar de la forma HH-MM: ")
        hora20 = input("Digite el rango superior a buscar de la forma HH-MM: ")

        fechaInventada1 = "2000-01-12 " + hora10 + ":01"
        fechaInventada2 = "2011-02-22 " + hora20 + ":02"

        hora1 = controller.aproximar(fechaInventada1)
        hora2 = controller.aproximar(fechaInventada2)

        accidente, server = controller.horasRango(cont, hora1, hora2)
        print("\nEl total de accidentes reportados entre ", hora10, "y", hora20, "son ", accidente)

        maximo_val = 0
        for k in server:
            if maximo_val < server[k]:
                maximo_val = server[k]
                severidad = k
        porcetaje = (maximo_val/accidente)*100
        print("La severidad con más accidentes es ", severidad, "con ", maximo_val)
        print("El porcentaje entre la severidad y los accidentes totales es el: ", round(porcetaje, 2), "%")


    else:
        sys.exit(0)
sys.exit(0)
