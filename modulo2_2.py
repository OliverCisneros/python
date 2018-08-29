import pandas as pd
pd.options.mode.chained_assignment = None #para que ignore advertencias de deprecado

df = pd.read_csv("velocidades.csv")
print("Registros en BD:")
print(df.count().sum())
print("Vehiculos en la BD:")
print(len(df["Vehiculo"].unique()))
print(df["Vehiculo"].unique())
print("Cantidad de dias y rango:")
print("Dias: {}   De: {}  A: {}".format(len(df["fecha"].unique()),
                                        df['fecha'].min(),
                                        df['fecha'].max()))

df["fecha"] = pd.to_datetime(df['fecha'], yearfirst=True)

mapaMesFecha = {}
for a in df['fecha']:
    key = a.strftime('%Y-%m')
    if key in mapaMesFecha:
        mapaMesFecha[key] = a.day if a.day > int(mapaMesFecha[key]) else mapaMesFecha[key]
    else:
        mapaMesFecha[key] = a.day

listMesesCompletos = []
for k,v in mapaMesFecha.items():
    mes = k.split('-')[1]
    meses31 = [1,3,5,7,8,10,12]
    meses30 = [2,4,6,9,11]
    if int(mes) == 2:
        if int(v) == 28:
            listMesesCompletos.append(k)
    elif int(mes) in meses31:
        if int(v) == 31:
            listMesesCompletos.append(k)
    elif int(mes) in meses30:
        if int(v) == 30:
            listMesesCompletos.append(k)


print("Los meses completos son: {}".format(len(listMesesCompletos)))

print("Horario de {}  a {}".format(df['hora'].min(),
                                   df['hora'].max()))
idmaxvel = df['velocidad'].idxmax()
print("Maxima velocidad: {}  y el vehiculo fue: {}".format(df.ix[idmaxvel,'velocidad'],
                                                          df.ix[idmaxvel,'Vehiculo']))

regOver80 = df[df['velocidad']>80]
#otra forma regOver80 = df.loc[df['velocidad']>80, ['Vehiculo']]
print("Sobrepasaron el limite de velocidad {} vehiculos y fueron : {}".
      format(len(regOver80['Vehiculo'].unique()),
             regOver80['Vehiculo'].unique()))

regOver80['hora'] = pd.to_datetime(regOver80['hora'],format= '%H:%M:%S' ).dt.strftime('%H')
print("La hora con mayor frecuencia de exesos es: {}".format(regOver80['hora'].mode().iloc[0]))

for i,v in df.groupby(df['fecha'].dt.strftime('%Y-%m'))["velocidad"].mean().items():
    if i in listMesesCompletos:
        print("Mes: {}   Velocidad promedio: {}".format(i, v))


