import csv

def leer_csv(csvs):
    '''
    Función que lee un archivo csv, lo imprime en pantalla y lo retorna
    '''
    with open(csvs, 'r') as f:
        csv_file = csv.reader(f)
        for row in csv_file:
            print(row)
    return csv_file

csv_equipos = leer_csv('equipo.csv')
csv_partidos = leer_csv('partidos.csv')
