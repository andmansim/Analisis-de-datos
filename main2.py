import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

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

#Agrupamos y contamos las veces que han jugado en casa y fuera
df_ganadorhome= df_ganador['home_team'].value_counts()
df_ganadoraway = df_ganador['away_team'].value_counts()
print(df_ganadorhome)
print(df_ganadoraway)

#Contamos las veces que ha ganado cada equipo
df_ganador = df_ganador['winner'].value_counts()
print(df_ganador)

#Contamos cuantas veces ha marcado gol el jugador 
print(df_goles.columns)
df_golesjugadores = df_goles['scorer'].value_counts()
print(df_golesjugadores)

