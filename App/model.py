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
from DISClib.DataStructures import listiterator as it
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
    analyzer['hour'] = om.newMap(omaptype='RBT',
                                    comparefunction= compareHours)

    return analyzer

# Funciones para agregar informacion al catalogo


# ==============================
# Funciones de consulta
# ==============================

def addAccident(analyzer, accident):

    lt.addLast(analyzer["accident"], accident["ID"])
    updateDate(analyzer['date'], accident)
    updateHour(analyzer['hour'], accident)
    
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


def updateHour(map, accident):

    fecha = accident["Start_Time"]
    hora = aproximar(fecha)
    ya = om.get(map, hora)
    if ya is None:
        valorr = NewEntry1(accident)
        om.put(map, hora, valorr)
    else:
        valorr = me.getValue(ya)
    updateValue1(valorr, accident)


def aproximar(fecha):
    
    fecha = fecha[0:17] +'00'
    fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    horas = fecha.time()
    minutos = horas.minute
    if minutos > 30:
        minutos = 60-minutos
        horas = (fecha + datetime.timedelta(minutes= minutos)).time()
        horas = str(horas)[0:2] +'00'
    elif minutos < 15:
        horas = str(horas)[0:2] + '00'
    else:
        horas = str(horas)[0:2] + '30'
    horas = int(horas)

    return horas
    
    


def NewEntry(accident):
    
    entry = {'list': None,
             'severidad': None}
    entry['list'] = lt.newList('ARRAY_LIST', compareIds)
    entry['severidad'] = m.newMap(30, 
                                    maptype='PROBING', 
                                    loadfactor=0.5,
                                    comparefunction= compareSeveridad)
    entry['estado'] = m.newMap(30, 
                                maptype='PROBING', 
                                loadfactor=0.5,
                                comparefunction= compareEstate)
    return entry



def NewEntry1(accident):

    entry = {'list': None,
             'severidad': None}
    entry['list'] = lt.newList('ARRAY_LIST', compareIds)
    entry['severidad'] = m.newMap(30, 
                                    maptype='PROBING', 
                                    loadfactor=0.5,
                                    comparefunction= compareSeveridad)
    return entry


def updateValue1(valor, accident):
    
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
        lt.addLast(valor1['lst_id'], accident['ID'])
    
    return valor



def updateValue(valor, accident):

    lista = valor["list"]
    lt.addLast(lista, accident["ID"])
    entra = m.get(valor["severidad"], accident["Severity"])
    estado = m.get(valor["estado"], accident["State"])
    if entra is None:
        lista2 = lt.newList('ARRAY_LIST')
        dicci = {}
        dicci['severidad'] = accident["Severity"]
        lt.addLast(lista2, accident["ID"])
        dicci['lst_id'] = lista2
        m.put(valor["severidad"], accident["Severity"], dicci)
    else:
        valor1 = me.getValue(entra)
        lt.addLast(valor1['lst_id'], accident['ID'])

    if estado is None:
        lista3 = lt.newList('ARRAY_LIST')
        diccit = {}
        diccit['estado'] = accident["State"]
        lt.addLast(lista3, accident["ID"])
        diccit['lst_estado'] = lista3
        m.put(valor["estado"], accident["State"], diccit)
    else:
        valor2 = me.getValue(estado)
        lt.addLast(valor2['lst_estado'], accident['ID'])

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
        


def A_antesFecha(analyzer, fecha):
    kmin = om.minKey(analyzer["date"])
    keys = om.keys(analyzer["date"], kmin, fecha)
    itera = it.newIterator(keys)
    accidente = 0
    numeroA = 0
    
    while it.hasNext(itera):
        llave = it.next(itera)
        ll = om.get(analyzer["date"], llave)

        valores = me.getValue(ll)
        
        accidente += lt.size(valores["list"])
        if numeroA <= lt.size(valores["list"]):
            numeroA = lt.size(valores["list"])
            date = llave
    print("La fecha con más accidentes es: ", date, "con ", numeroA)

    return accidente


def accidentesRango(analyzer, fecha1, fecha2):
    llaves = om.keys(analyzer["date"], fecha1, fecha2)
    itera = it.newIterator(llaves)
    accidente = 0
    server ={}

    while it.hasNext(itera):
        llave = it.next(itera)
        llv = om.get(analyzer["date"], llave)
        va = me.getValue(llv)
        accidente += lt.size(va["list"])
        valor_mapa = m.valueSet(va["severidad"])

        itera1 = it.newIterator(valor_mapa)
        while it.hasNext(itera1):
            valor_m = it.next(itera1)
            id_severidad = valor_m["severidad"]
            if id_severidad not in server.keys():
                server[id_severidad] = lt.size(valor_m["lst_id"])
            else:
                server[id_severidad] += lt.size(valor_m["lst_id"])

    return accidente, server


def accidentesRango1(analyzer, fecha1, fecha2):
    llaves = om.keys(analyzer["date"], fecha1, fecha2)
    itera = it.newIterator(llaves)
    accidente1 = 0
    server2 ={}

    while it.hasNext(itera):
        llave = it.next(itera)
        llv = om.get(analyzer["date"], llave)
        va = me.getValue(llv)
        accidente1 += lt.size(va["list"])
        valor_mapa = m.valueSet(va["estado"])

        itera1 = it.newIterator(valor_mapa)
        while it.hasNext(itera1):
            valor_m = it.next(itera1)
            id_severidad = valor_m["estado"]
            if id_severidad not in server2.keys():
                server2[id_severidad] = lt.size(valor_m["lst_estado"])
            else:
                server2[id_severidad] += lt.size(valor_m["lst_estado"])

    return accidente1, server2
    

def horasRango(analyzer, hora1, hora2):
    
    llav = om.keys(analyzer['hour'], hora1, hora2) 
    itera = it.newIterator(llav)
    accidente1 = 0
    server2 ={}

    while it.hasNext(itera):
        llave = it.next(itera)
        llv = om.get(analyzer["hour"], llave)
        va = me.getValue(llv)
        accidente1 += lt.size(va["list"])
        valor_mapa = m.valueSet(va["severidad"])

        itera1 = it.newIterator(valor_mapa)
        while it.hasNext(itera1):
            valor_m = it.next(itera1)
            id_severidad = valor_m["severidad"]
            if id_severidad not in server2.keys():
                server2[id_severidad] = lt.size(valor_m["lst_id"])
            else:
                server2[id_severidad] += lt.size(valor_m["lst_id"])

    return accidente1, server2



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


def compareHours(h1, h2):
    
    if (h1 == h2):
        return 0
    elif h1 > h2:
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

def compareEstate(e1, e2):
    if e1 == me.getKey(e2):
        return 0
    return 1