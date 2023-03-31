

# Neuralworks challenge

Este repositorio ha sido creado con el fin de desarrollar el desafío tecnico provisto por Neuralworks para Machine Learning Engineer.

Este repo contiene (1) rama development la cual fue utilizada para el desarrollo de este desafío y (2) rama main para el despliegue del algoritmo en Google Cloud Run con CI/CD implementado sobre la misma rama.

## tl-tr



## Problema
Te encuentras trabajando en un equipo conformado por varios Data Scientists. Uno de ellos, Juan, ha terminado sus experimentos y te ha pedido que habilites un servicio para que su modelo pueda ser consumido por varios actores fuera del equipo.
Juan escribió en un Jupyter Notebook una serie de modelos para predecir la probabilidad de atraso de los vuelos que aterrizan o despegan del aeropuerto de Santiago de Chile (SCL). Para eso utilizó un dataset de datos públicos y reales donde cada fila corresponde a un vuelo que aterrizó o despegó de SCL. Para cada vuelo se cuenta con la siguiente información:
1. Fecha-I: Fecha y hora programada del vuelo.
2. Vlo-I: Número de vuelo programado.
3. Ori-I: Código de ciudad de origen programado.
4. Des-I: Código de ciudad de destino programado.
5. Emp-I: Código aerolínea de vuelo programado.
6. Fecha-O: Fecha y hora de operación del vuelo.
7. Vlo-O: Número de vuelo de operación del vuelo.
8. Ori-O: Código de ciudad de origen de operación
9. Des-O: Código de ciudad de destino de operación.
10. Emp-O: Código aerolínea de vuelo operado.
11. DIA: Día del mes de operación del vuelo.
12. MES: Número de mes de operación del vuelo.
13. AÑO: Año de operación del vuelo.
14. DIANOM: Día de la semana de operación del vuelo.
15. TIPOVUELO : Tipo de vuelo, I =Internacional, N =Nacional.
16. OPERA: Nombre de aerolínea que opera.
17. SIGLAORI: Nombre ciudad origen.
18. SIGLADES: Nombre ciudad destino.

## El desafío

El desafío contempla las siguientes instrucciones las cuales deben ser entregadas en un plazo maximo de 5 dias desde la recepción del desafío.

Tu desafío consiste en tomar el trabajo de Juan y exponerlo para que sea utilizado por el resto de la compañia:
1. Escoge el modelo que a tu criterio tenga una mejor performance, argumentando tu decisión.

2. Implementa cambios sobre el modelo escogiendo la o las técnicas que prefieras buscando mejorar los resultados. Te recomendamos dejar los intentos que no lograron mejorar los resultados.

3. Serializa el modelo seleccionado (puede ser de los construidos en el punto 2) e implementa una API REST para poder predecir atrasos de nuevos vuelos.

4. Automatiza el proceso de build y deploy de la API, utilizando uno o varios servicios cloud. Argumenta tu decisión sobre los servicios utilizados.

5. Realiza pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto debes utilizar esta herramienta y presentar las métricas obtenidas. ¿Cómo podrías mejorar el performance de las pruebas anteriores?
## Desarrollo

El repositorio cuenta con la siguientes estructura:


# Neuralworks challenge

Este repositorio ha sido creado con el fin de desarrollar el desafío tecnico provisto por Neuralworks para Machine Learning Engineer.

Este repo contiene (1) rama development la cual fue utilizada para el desarrollo de este desafío y (2) rama main para el despliegue del algoritmo en Google Cloud Run con CI/CD implementado sobre la misma rama.


## Problema
Te encuentras trabajando en un equipo conformado por varios Data Scientists. Uno de ellos, Juan, ha terminado sus experimentos y te ha pedido que habilites un servicio para que su modelo pueda ser consumido por varios actores fuera del equipo.
Juan escribió en un Jupyter Notebook una serie de modelos para predecir la probabilidad de atraso de los vuelos que aterrizan o despegan del aeropuerto de Santiago de Chile (SCL). Para eso utilizó un dataset de datos públicos y reales donde cada fila corresponde a un vuelo que aterrizó o despegó de SCL. Para cada vuelo se cuenta con la siguiente información:
1. Fecha-I: Fecha y hora programada del vuelo.
2. Vlo-I: Número de vuelo programado.
3. Ori-I: Código de ciudad de origen programado.
4. Des-I: Código de ciudad de destino programado.
5. Emp-I: Código aerolínea de vuelo programado.
6. Fecha-O: Fecha y hora de operación del vuelo.
7. Vlo-O: Número de vuelo de operación del vuelo.
8. Ori-O: Código de ciudad de origen de operación
9. Des-O: Código de ciudad de destino de operación.
10. Emp-O: Código aerolínea de vuelo operado.
11. DIA: Día del mes de operación del vuelo.
12. MES: Número de mes de operación del vuelo.
13. AÑO: Año de operación del vuelo.
14. DIANOM: Día de la semana de operación del vuelo.
15. TIPOVUELO : Tipo de vuelo, I =Internacional, N =Nacional.
16. OPERA: Nombre de aerolínea que opera.
17. SIGLAORI: Nombre ciudad origen.
18. SIGLADES: Nombre ciudad destino.

## El desafío

El desafío contempla las siguientes instrucciones las cuales deben ser entregadas en un plazo maximo de 5 dias desde la recepción del desafío.

Tu desafío consiste en tomar el trabajo de Juan y exponerlo para que sea utilizado por el resto de la compañia:
1. Escoge el modelo que a tu criterio tenga una mejor performance, argumentando tu decisión.

2. Implementa cambios sobre el modelo escogiendo la o las técnicas que prefieras buscando mejorar los resultados. Te recomendamos dejar los intentos que no lograron mejorar los resultados.

3. Serializa el modelo seleccionado (puede ser de los construidos en el punto 2) e implementa una API REST para poder predecir atrasos de nuevos vuelos.

4. Automatiza el proceso de build y deploy de la API, utilizando uno o varios servicios cloud. Argumenta tu decisión sobre los servicios utilizados.

5. Realiza pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto debes utilizar esta herramienta y presentar las métricas obtenidas. ¿Cómo podrías mejorar el performance de las pruebas anteriores?
## Desarrollo

El repositorio cuenta con la siguientes estructura:

```bash
.
├── README.md
├── documentos
│   ├── Challenge Machine Learning Engineer - NeuralWorks.pdf
│   └── desafio_latam.pdf
├── main
│   ├── Dockerfile
│   ├── __pycache__
│   │   └── main.cpython-38.pyc
│   ├── main.py
│   ├── model
│   │   ├── lgbm_model_late_flight_v1.pkl
│   │   └── lgbm_model_late_flight_v1.txt
│   ├── requirements.txt
│   └── utils
│       ├── __pycache__
│       │   └── functions.cpython-38.pyc
│       ├── delay_ratio_tables
│       │   ├── Last 1 Months_delay_ratio_DIA_table.pkl
│       │   ├── Last 1 Months_delay_ratio_MES_table.pkl
│       │   ├── Last 1 Months_delay_ratio_OPERA_table.pkl
│       │   ├── Last 1 Months_delay_ratio_SIGLADES_table.pkl
│       │   ├── Last 1 Months_delay_ratio_periodo_dia_table.pkl
│       │   ├── Last 3 Months_delay_ratio_DIA_table.pkl
│       │   ├── Last 3 Months_delay_ratio_MES_table.pkl
│       │   ├── Last 3 Months_delay_ratio_OPERA_table.pkl
│       │   ├── Last 3 Months_delay_ratio_SIGLADES_table.pkl
│       │   ├── Last 3 Months_delay_ratio_periodo_dia_table.pkl
│       │   ├── historical_delay_ratio_MES.pkl
│       │   ├── historical_delay_ratio_OPERA.pkl
│       │   ├── historical_delay_ratio_SIGLADES.pkl
│       │   └── historical_delay_ratio_periodo_dia.pkl
│       └── functions.py
└── notebooks
    ├── CURL test
    ├── Docker commands
    ├── dataset_SCL.csv
    ├── preprocessing_pipeline.ipynb
    ├── synthetic_features.csv
    ├── testing.csv
    ├── to-expose-JA.ipynb
    └── to-expose.ipynb
```
Donde:


1. **documentos:** Contiene (1) el documento entregado para realizar el desafío junto a (2) un documento desarrollado por el autor el cual fue entregado a LATAM en el año 2021 para un proceso similar donde resulto ganador.
2. **main:** Contiene todo el codigo principal utilizado para realizar el despliegue correspondiente del algoritmo seleccionado en Google Cloud Run utilizando Dockerfile. Los archivos dentro de esta carpeta son:
    * 2.1 Dockerfile: Archivo Docker construido para crear imagen en Google Container Registry.
    * 2.2 main.py: Codigo python construido con el fin de habilitar API REST con el fin de obtener la probabilidad de que un vuelo se atrase. Este      aplicacion fue construida utilizando [Fast-API](https://fastapi.tiangolo.com/) para crear la API y [Uvicorn](https://www.uvicorn.org/) para exponerla. El algoritmo utilizado corresponde a [LightGBM](https://lightgbm.readthedocs.io/en/v3.3.2/) en adelante **LGBM** cuyo supuesto y seleccion se explica mas adelante.
    * 2.3 model: Carpeta que contiene el algoritmo serializado utilizando pickle y Booster (propio de LGBM) para utilizar segun conveniencia.
    * 2.4 requirements.txt: Archivo con librerias requeridas para el funcionamiento y despliegue de la aplicación.
    * 2.5 utils: Carpeta que contiene (1) codigo functions.py construido para administrar y disponibilizar funciones utilizadas en el desarrollo y construccion de la aplicación. (2) carpeta delay_ratio_tables la cual contiene tablas serializadas con data procesada con diversas frecuencias de atraso utilizadas al momento de predecir. (Variables importantes del algoritmo).
3. **notebooks:** Carpeta que contiene dataset entregado para el desafio (dataset_SCL.csv), dataset creado para testear el algoritmo (testing.csv), archivo CURL test el cual contiene ejemplos de request para la API, Docker commands para guardar comandos necesarios gcloud para el despliegue de la APP en Google Cloud Run, **to-expose.ipynb** codigo notebook con proceso de entrenamiento entregado para desarrollar el desafío ("el trabajo de Juan"), **to-expose-JA.ipynb** codigo notebook con proceso de (1) revisión, (2) validación de algoritmos, (3) propuesta con mejora, (4) serialización de tablas y modelo, y **preprocessing_pipeline.ipynb** codigo notebook el cual contiene el preprocesamiento y funciones necesarias utilizadas en la construccion de metodo "POST" endpoint /predict_delay_probability para obtener la probabilidad de retraso.

## to-expose-JA:




