import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

def leer_csv(ruta, indice):
    with open (ruta, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        df = pd.DataFrame(reader, columns = indice)
    return df

df_equipo = leer_csv('equipo.csv', ['nombre', 'img', 'pais', 'numero'])
df_partidos = leer_csv('partidos.csv', ['fecha', 'hora', 'equipo1', 'equipo2', 'goles1', 'goles2'])#NO TENGO NI ZORRA DE QUE COÑO VA ESTE PUTO CSV

