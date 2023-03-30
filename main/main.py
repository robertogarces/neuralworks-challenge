# Imports locales
from fastapi import FastAPI
from pydantic import BaseModel
import platform
import lightgbm as lgb
import pandas as pd
import numpy as np
import os
from utils.functions import utils
import pickle
import warnings
warnings.filterwarnings('ignore')

# Definiendo APP
app = FastAPI()

#Inicializar utils functions
u = utils()

# Definiendo esquema
class InputData(BaseModel):
    OPERA: str
    SIGLADES: str
    FECHA_PROGRAMADA: str

# Cargar el modelo
model_path = '../main/model/lgbm_model_late_flight_v1.txt'
model = lgb.Booster(model_file=model_path)

# API endpoints
@app.get("/model_status")
async def model_status():
    
    # Revision del status del modelo
    if model:
        model_status = 'Modelo activo y cargado 🔥'
    else:
        model_status = 'Modelo no ha sido cargado ❤️‍🩹'

    model_file = os.path.basename(model_path)
    
    # Devuelve el estado del modelo entregando info
    return {
        'python version': platform.python_version(), #Version de Python
        'model_status': model_status, #Estado del modelo
        'model_type': 'LGBM', #Tipo de algoritmo
        'model_file': model_file, #Algoritmo entrenado
        'model_input_variables': ['OPERA', 'SIGLADES', 'FECHA_PROGRAMADA'], #INPUT variables
        'input_example': {'OPERA': 'Sky Airline','SIGLADES':'Calama', 'FECHA_PROGRAMADA':'2017-11-27 13:00:00'} #Ejemplo
    }

@app.post("/predict_delay_probability")
async def predict_delay_probability(input_data: InputData):

    # Cargar tablas para creacion de variables
    directory = '../main/utils/delay_ratio_tables'
    utils_tables = u.load_pickles_from_directory(directory)
    tables = utils_tables.keys()

    # Columnas necesarias para predecir
    cols = ['historical_delay_ratio_SIGLADES', 'historical_delay_ratio_OPERA',
       'historical_delay_ratio_MES', 'historical_delay_ratio_periodo_dia',
       'Last 1 Months_delay_ratio_OPERA', 'Last 1 Months_delay_ratio_DIA',
       'Last 3 Months_delay_ratio_DIA']
    
    # Convertir input en dataframe
    input_df = pd.DataFrame([input_data.dict()])
    input_df.rename(columns={'FECHA_PROGRAMADA':'Fecha-I'}, inplace=True) #Modificar nombre para mantener variable segun entrenamiento

    #Crear dataset para predecir
    input_df['periodo_dia'] = input_df['Fecha-I'].apply(u.get_periodo_dia) #Creacion de campo periodo dia
    input_df['DIA'] = pd.to_datetime(input_df['Fecha-I']).dt.day #Creacion de campo DIA
    input_df['MES'] = pd.to_datetime(input_df['Fecha-I']).dt.month #Creacion de campo MES
    input_df = u.get_delay_ratios(input_df, utils_tables, tables) #Merging con tablas con frecuencia de atraso
    input_df = input_df[cols] #Filtrar columnas encesarias para predecir
    input_df = input_df.iloc[0]
    # Prediccion
    probs = np.round(model.predict(input_df)[0],2)
    y_pred = ['Alta probabilidad de atraso' if probs > 0.5 else 'Baja probabilidad de atraso']
    
    # Return the predictions
    return {'delay_probability': probs, 'clase': y_pred, 'build_deploy': 'True'} #to deploy