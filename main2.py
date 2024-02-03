import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_goles = pd.read_csv('goles.csv', encoding='utf-8', delimiter=',')
df_ganador = pd.read_csv('winner.csv', encoding='utf-8', delimiter=',')

#Vemos la información de cada DataFrame
print('\n'+'Información de los DataFrames:')
print('\n'+'Goles:')
print(df_goles.info())
print(df_goles.columns)
print('\n'+'Ganador:')
print(df_ganador.info())
print(df_ganador.columns)
#No hay ningún valor nulo

print('\n'+ 'Representaciones gráficas:')
#Agrupamos por team(Equipo que metió gol en dicho minuto) y hacemos la media del minuto
df_goles_media = df_goles.groupby('team').mean()

#Representamos los 15 equipos con mayor media de goles
df_goles_media = df_goles_media.sort_values(by='minute', ascending=False)
df_goles_media = df_goles_media.head(15)
print(df_goles_media)

plt.bar(df_goles_media.index, df_goles_media['minute'])
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9, top=0.9)
plt.show()


#Agrupamos y contamos las veces que han jugado en casa y fuera
df_ganadorhome= df_ganador['home_team'].value_counts()
df_ganadoraway = df_ganador['away_team'].value_counts()

#Representamos los 15 equipos con mayor media de goles en casa y fuera
df_ganadorhome = df_ganadorhome.sort_values(ascending=False)
df_ganadorhome = df_ganadorhome.head(15)
plt.bar(df_ganadorhome.index, df_ganadorhome)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9, top=0.9)
plt.show()

df_ganadoraway = df_ganadoraway.sort_values(ascending=False)
df_ganadoraway = df_ganadoraway.head(15)
plt.bar(df_ganadoraway.index, df_ganadoraway)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9, top=0.9)
plt.show()



#Contamos las veces que ha ganado cada equipo
print('\n'+ 'Las veces que ha ganado cada equipo:')
df_ganador = df_ganador['winner'].value_counts()
print(df_ganador)

#Contamos cuantas veces ha marcado gol el jugador 

df_golesjugadores = df_goles['scorer'].value_counts()
print(df_golesjugadores)

