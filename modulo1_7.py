import csv, json
listaFinal = []
with open('TodasLasNoticias.csv', 'r',encoding="utf8") as data:
    fileReader = csv.reader(data, delimiter=',', quotechar='"')
    for linea in fileReader:
        lista = str(linea).split(',')
        mapa = {}
        mapa['fecha'] = lista[0]
        mapa['titulo'] = lista[1]
        mapa['descripcion'] = lista[3]
        mapa['categoria'] = lista[4]
        listaFinal.append(mapa)

print(listaFinal)