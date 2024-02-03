import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_goles = pd.read_csv('goalscorers.csv', encoding='utf-8', delimiter=',')
df_ganador = pd.read_csv('winner.csv', encoding='utf-8', delimiter=',')

#Vemos la información de cada DataFrame
print(df_goles.info())
print(df_goles.columns)

print(df_ganador.info())
print(df_ganador.columns)
#No hay ningún valor nulo

#Agrupamos por team y hacemos la media del minuto
df_goles_media = df_goles.groupby('team').mean()
print(df_goles_media)
#Representamos los 15 equipos con mayor media de goles
df_goles_media = df_goles_media.sort_values(by='minute', ascending=False)
df_goles_media = df_goles_media.head(15)
print(df_goles_media)
df_goles_media.plot(kind='bar')
plt.show()

#Agrupamos y contamos las veces que han jugado en casa y fuera
df_ganadorhome= df_ganador['home_team'].value_counts()
df_ganadoraway = df_ganador['away_team'].value_counts()
print(df_ganadorhome)
print(df_ganadoraway)
#Representamos los 15 equipos con mayor número de partidos jugados en casa
df_ganadorhome = df_ganadorhome.head(15)
df_ganadorhome.plot(kind='bar')
plt.show()
#Representamos los 15 equipos con menor número de partidos jugados fuera
df_ganadoraway = df_ganadoraway.head(15)
df_ganadoraway.plot(kind='bar')
plt.show()


#Contamos las veces que ha ganado cada equipo
df_ganador = df_ganador['winner'].value_counts()
print(df_ganador)

#Contamos cuantas veces ha marcado gol el jugador 
print(df_goles.columns)
df_golesjugadores = df_goles['scorer'].value_counts()
print(df_golesjugadores)

