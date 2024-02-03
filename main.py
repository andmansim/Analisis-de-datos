import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

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
print(df_equipo.info())
print(df_partidos.info())
#No hay ningún valor nulo

#transformamos las columnas de numero a enteros
df_equipo['numero'] = df_equipo['numero'].astype(int)

#Ordenamos los equipos por numero
df_equipo = df_equipo.sort_values(by='numero', ascending=True)
print(df_equipo.head())

# Representación de los equipos por país con nombres rotados
plt.bar(df_equipo['pais'].value_counts().index, df_equipo['pais'].value_counts())
plt.xticks(rotation=45, ha='right')  # Ajusta la rotación y alineación horizontal de los nombres
plt.xlabel('País')
plt.ylabel('Número de Equipos')
plt.title('Número de Equipos por País')
plt.tight_layout()
plt.show()