import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
#leemos los datos
def leer_csv(ruta, indice):
    #Función encargada en leer y asignar los nombres de las columnas correspondientes
    with open (ruta, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        df = pd.DataFrame(reader, columns = indice)
    return df


#Leemos cada csv y creamos los DataFrames correspondientes
df_equipo = leer_csv('equipo.csv', ['nombre', 'img', 'pais', 'numero'])
df_partidos = leer_csv('partidos.csv', ['dia', 'equipo1', 'equipo2', 'numero1', 'numero2', 'numero3'])

#Vemos la información de cada DataFrame
print('\n'+'Información de los DataFrames:')
print('\n'+'Equipo:')
print(df_equipo.info())
print('\n'+'Partidos:')
print(df_partidos.info())
#No hay ningún valor nulo

#Nos damos cuenta que las 3 últimas columnas no sirven para nada, entonces vamos a quitar 1 y las otras las cambiaremos 
# por posible goles que haya metido cada equipo
df_partidos = df_partidos.drop(columns=['numero1', 'numero2', 'numero3'])
df_partidos['goles1'] = np.random.randint(0, 5, df_partidos.shape[0])
df_partidos['goles2'] = np.random.randint(0, 5, df_partidos.shape[0])
print(df_partidos.head())


#Vamos a hacer un análisis de los datos

#Ordenamos los equipos por numero
df_equipo = df_equipo.sort_values(by='numero', ascending=True)
print('\n'+'Ordenamos los equipos por número:')
print(df_equipo.head())

#Calculamos la media de goles por partido
media_goles = (df_partidos['goles1'] + df_partidos['goles2']).mean()
print('\n'+'Media de goles por partido:', media_goles)

#Calculamos el equipo con más y menos goles

df_equipo['goles'] = df_equipo['numero'] * 2
print('\n'+'Equipo con más goles:', df_equipo[df_equipo['goles'] == df_equipo['goles'].max()])
print('\n'+'Equipo con menos goles:', df_equipo[df_equipo['goles'] == df_equipo['goles'].min()])

#Varianza y desviación estándar de los goles
varianza_goles = (df_partidos['goles1'] + df_partidos['goles2']).var()
desviacion_goles = (df_partidos['goles1'] + df_partidos['goles2']).std()
print('\n'+'Varianza de los goles:', varianza_goles)
print('\n'+'Desviación estándar de los goles:', desviacion_goles)


# Representación de los equipos por país 
plt.bar(df_equipo['pais'].value_counts().index, df_equipo['pais'].value_counts())
plt.xticks(rotation=45, ha='right')  # Ajusta la rotación y alineación horizontal de los nombres
plt.xlabel('País')
plt.ylabel('Número de Equipos')
plt.title('Número de Equipos por País')
plt.tight_layout()
plt.show()