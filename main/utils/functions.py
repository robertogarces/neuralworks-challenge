import os, json, pickle
from datetime import datetime
import pandas as pd

class utils:

    def __init__(self) -> None:
        print("Utils inicializado correctamente")


    def load_pickles_from_directory(self, directory):
        """
        Cargar todos los archivos pkl en el directorio especificado

        Args:
            directory (str): Directorio que contiene pkl files

        Returns:
            dict: Un diccionario que contiene los objetos pkl cargados, donde las claves son los nombres de archivo (sin la extensión '.pkl').
        """
        pickles = {}
        for filename in os.listdir(directory):
            if filename.endswith('.pkl'):
                path = os.path.join(directory, filename)
                with open(path, 'rb') as file:
                    pickled_object = pickle.load(file)
                key = filename[:-4]  # remove the '.pkl' extension from the filename
                pickles[key] = pickled_object
        return pickles


    #Funcion para crear periodo del dia
    def get_periodo_dia(self, fecha):
        fecha_time = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S').time()
        mañana_min = datetime.strptime("05:00", '%H:%M').time()
        mañana_max = datetime.strptime("11:59", '%H:%M').time()
        tarde_min = datetime.strptime("12:00", '%H:%M').time()
        tarde_max = datetime.strptime("18:59", '%H:%M').time()
        noche_min1 = datetime.strptime("19:00", '%H:%M').time()
        noche_max1 = datetime.strptime("23:59", '%H:%M').time()
        noche_min2 = datetime.strptime("00:00", '%H:%M').time()
        noche_max2 = datetime.strptime("4:59", '%H:%M').time()
        
        if(fecha_time > mañana_min and fecha_time < mañana_max):
            return 'mañana'
        elif(fecha_time > tarde_min and fecha_time < tarde_max):
            return 'tarde'
        elif((fecha_time > noche_min1 and fecha_time < noche_max1) or
            (fecha_time > noche_min2 and fecha_time < noche_max2)):
            return 'noche'
        
    def get_delay_ratios(self, dataset, data_pkl, tables):
        for table in tables:
            data = data_pkl[table]
            try:
                dataset = dataset.merge(data, how='left', on=data.columns[0])
            except:
                pass
        return dataset