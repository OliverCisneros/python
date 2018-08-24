class miclase:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def myfunc(self):
        print("Hello my name is {}".format(self.nombre))

p1=miclase("Pedro",34)
p1.myfunc()
del p1.edad
print(p1.edad)

import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x,indent=4, sort_keys=True)

print(y)


f = open("TodasLasNoticias.csv","r")
for x in f:
    print(x)


import csv
mapa = {}
with open('TodasLasNoticias.csv', 'r') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in fileReader:
        palabras = str(line).split()
        for palabra in palabras:
            if palabra in mapa:
                mapa[palabra] = mapa[palabra] + palabras.count(palabra)
            else:
                mapa[palabra] = palabras.count(palabra)
print(json.dumps(mapa,indent=4, sort_keys=True))



