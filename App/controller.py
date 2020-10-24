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

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    return analyzer


def accidentesFecha(analyzer, fecha):
    
    fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    return model.accidentesFecha(analyzer, fecha.date())


def A_antesFecha(analyzer, fecha):
    fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    return model.A_antesFecha(analyzer, fecha.date())


def accidentesRango(analyzer, fecha1, fecha2):
    fecha1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d')
    fecha2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d')
    return model.accidentesRango(analyzer, fecha1.date(), fecha2.date())


def accidentesRango1(analyzer, fecha1, fecha2):
    fecha1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d')
    fecha2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d')
    return model.accidentesRango1(analyzer, fecha1.date(), fecha2.date())


def aproximar(fechaa):
    return model.aproximar(fechaa)


def horasRango(analyzer, hora1, hora2):
    return model.horasRango(analyzer, hora1, hora2)

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def altura(arbol):
    return model.altura(arbol)

def indexSize(arbol):
    return model.indexSize(arbol)