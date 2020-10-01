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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

def newAnalyzer():

    analyzer = {'accident': None,
                'date': None}

    analyzer['accident'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['date'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)

    return analyzer

# Funciones para agregar informacion al catalogo


# ==============================
# Funciones de consulta
# ==============================

def addAccident(analyzer, accident):

    lt.addLast(analyzer["accident"], accident["ID"])
    updateDate(analyzer['date'], accident)
    
    return analyzer


def updateDate(map, accident):

    date = accident["Start_Time"]
    accidente = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    accidente = accidente.date()
    esta = om.get(map, accidente)
    if esta is None:
        valor = NewEntry(accident)
        om.put(map, accidente, valor)
    else:
        valor = me.getValue(esta)
    updateValue(valor, accident)


def NewEntry(accident):
    
    entry = {'list': None,
             'severidad': None}
    entry['list'] = lt.newList('ARRAY_LIST', compareIds)
    entry['severidad'] = m.newMap(30, 
                                    maptype='PROBING', 
                                    loadfactor=0.5,
                                    comparefunction= compareSeveridad)
    return entry


def updateValue(valor, accident):

    lista = valor["list"]
    lt.addLast(lista, accident["ID"])
    entra = m.get(valor["severidad"], accident["Severity"])
    if entra is None:
        lista2 = lt.newList('ARRAY_LIST')
        dicci = {}
        dicci['severidad'] = accident["Severity"]
        lt.addLast(lista2, accident["ID"])
        dicci['lst_id'] = lista2
        m.put(valor["severidad"], accident["Severity"], dicci)
    else:
        valor1 = me.getValue(entra)
        lt.addLast(valor1['lst_id'], accident['Severity'])
    return valor
        

def altura(arbol):
    return om.height(arbol)

def indexSize(arbol):
    return om.size(arbol)


def accidentesFecha(analyzer, fecha):

    llv = om.get(analyzer["date"], fecha)
    acci = me.getValue(llv)
    lis = m.valueSet(acci['severidad'])
    return lis
        

    
    

# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(id1, id2):
    
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareSeveridad(s1, s2):

    if (s1 == me.getKey(s2)):
        return 0
    return 1 
