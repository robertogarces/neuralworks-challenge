

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

### Comentarios:

Si bien dentro del trabajo de Juan se realiza el split de data para el proceso de entrenamiento, en ningun punto es comparado con la data de testeo (para prevenir overfitting). Dado lo anterior, se vuelve a realizar split de data tomando 10% para testing, 20% para validacion, y 70% para entrenamiento. Dado el rendimiento del algoritmo se utliza calculo de [Lift curve](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871) para buscar el corte de probabilidad que permite obtener mayor probabilidad de exito en detectar atrasos.

1. Algoritmo 1: Regresion logistica entrenada por Juan:
        
      * - Performance y lift curve:
      * **Performance:** 
      * ![image](https://user-images.githubusercontent.com/41343847/229136420-4d789bb9-9f02-4abc-849c-d99305b8dd7b.png)
      * **Lift curves:** 
      * Training:
      * ![image](https://user-images.githubusercontent.com/41343847/229137794-20f3da12-fc78-45e1-b175-f9544ed180fc.png)
      * Validation:
      * ![image](https://user-images.githubusercontent.com/41343847/229138394-f9da7310-315a-4f85-92aa-3cf3b1c74553.png)
      * Testing:
      * ![image](https://user-images.githubusercontent.com/41343847/229138769-38015080-5542-44f5-9ab2-9363ea8fbd9f.png)

      * El performance del modelo, en si con este conjunto de datos y variables, en mi opinion no tiene el resultado necesario para realizar un despliegue en productivo.
      * La precision sobre la clase de interes (retraso) es de un 55% con un recall o sensibilidad del 3% (es capaz de detectar el 3% de los datos).
      * Mirando F1 score que combina ambas metricas (precision y recall) el performance es de 48% (peor que una moneda) por lo que un modelo dummy (ej. decir que todos son 0) performaria mejor.
      * No se percibe overfitting.
      * Dado el performance del modelo, se recomienda utilizar otras variables como condiciones meteorologicas, comportamientos ultimos x meses de aerolineas, destinos, etc.
      * Dado el desafío para este modelo entrenado por Juan, se recomienda utilizar un threshold de 0.4 para definir si el vuelo se atrasara o no segun estudio utilizando Lift Curve. (generalmente se usa para otro tipo de iniciativas pero en este caso podemos ajustar la probabilidad optima para estas condiciones.)
      * Otra manera de optimizar el corte de probabilidad es utilizando precision-recall curve.

2. Algoritmo 2: XGBoost classifier entrenado por Juan
      * **Performance:** 
      * ![image](https://user-images.githubusercontent.com/41343847/229139912-c0320b6b-65d4-46ea-930c-9faa9ab5f346.png)
      * **Variables importantes:**
      * ![image](https://user-images.githubusercontent.com/41343847/229140045-2ac0b286-d07c-4b34-8edd-2f206caf0714.png)
      * **Performance post feature selection:**
      * ![image](https://user-images.githubusercontent.com/41343847/229140281-c2a472f4-9613-428e-92ff-c51556e68f02.png)
      * No hay mejoras en el performance al cambiar de algoritmo. Dado que la tarea mas importante (en mi opinion) para este desafío es desplegar y configurar CI/CD se realizarán ajustes menores que buscan mejorar el performance.

3. Algoritmo 3: Modelos entrenados por Jaime

      * Mejoras y supuestos:
      * Se utiliza en un principio todo el dataset sin filtrar previamente por columnas subjetivamente seleccionadas.
      * Se percibe un error en calculo de frecuencias de atraso para las variables SIGLADES, OPERA, MES, DIA, TIPO_VUELO, temporada_alta, TIPO_VUELO y periodo_dia. Se corrige y se guardan calculos historicos de frecuencia de atraso (serializadas para su uso en prediccion).
      * Construccion de funcion que permite obtener la frecuencia de atraso para las columnas de interes en 1, 3, 6 y 12 meses (variable) bajo el supuesto de que el comportamiento de atrasos sobre los meses presentes deberian contribuir con el poder de prediccion. Por ej. Una aerolinea que en los ultimos meses ha tenido un alta frecuencia de atraso puede significar problemas de control de operaciones u otras condiciones las cuales hacen que sus vuelos se atrasen y por ende es importante entregarle este insight al modelo. Estas variables se calculan y se serializan para ser usadas en prediccion.
      * Para efectos de entrenamiento y rango de fechas del dataset entregado (2017) se usa 1 y 3 meses de comportamiento. A continuacion 3 graficos de ejemplo sobre variables calculadas.
      * Frecuencias de atraso por SIGLADES
      * ![image](https://user-images.githubusercontent.com/41343847/229143791-7e2de5bd-ac98-421a-b75b-d8cd2e4e6363.png)
      * Frecuencias de atraso por OPERA
      * ![image](https://user-images.githubusercontent.com/41343847/229143924-65ce8569-8b97-4c20-8157-a7d7d6602aa8.png)
      * Frecuencias de atraso por DIA
      * ![image](https://user-images.githubusercontent.com/41343847/229144027-49989ac0-308c-4fe6-8386-25851ccb069e.png)
      * Se mantiene proceso de creacion de dummies para variables categoricas.
      * Eliminacion de variables correlacionadas con threshold de 0.8 para evitar problema de multicolinealidad.
      * Eliminacion de variables poco significativas utilizando L1 regularization (lasso)
      * No se utilizar normalizacion dado que las variables se encuentran en valores entre 0 y 1.
      * No se eliminan outliers por conveniencia.
      * Seleccion de variables importantes utilizando threshold optimizado el cual mantiene performance y aumenta la velocidad de prediccion.

      * Resultados:
      
      * Regresion logistica:
      * ![image](https://user-images.githubusercontent.com/41343847/229144941-409a1035-29ee-41e9-a369-edbeb94ee49e.png)
      
      * XGBoost:
      
      * ![image](https://user-images.githubusercontent.com/41343847/229145022-af852d18-7a47-4679-87d8-13e95f1cdb73.png)
      * Dado el resultado con mejora sutil anterior, se utiliza LGBM
      
      * LGBM con optimizacion de hyperparametros configurado callback para prevenir overfitting:
      
      * ![image](https://user-images.githubusercontent.com/41343847/229145613-251950e6-aba4-4bcb-8885-d9807e7218b3.png)
      * **Lift curves:** 
      * Training:
      * ![image](https://user-images.githubusercontent.com/41343847/229146506-af6454e7-65bf-4e1d-bb5f-71a1501d5fb9.png)
      * Validation:
      * ![image](https://user-images.githubusercontent.com/41343847/229146536-1d6fa2a3-5a1a-40df-afe7-582cf1eefb93.png)
      * Testing:
      * ![image](https://user-images.githubusercontent.com/41343847/229146580-8375deac-fff8-4c59-8353-61c7d2d36c5a.png)
      * Dado que el modelo mejorado performa 16% mejor sin overfitting en F1 Score que el entrenado por Juan, se continuara el despliegue con este.

### Despliegue:

1. Variables necesarias para predecir:
      * Dado las siguientes variables, se utilizaran OPERA, SIGLADES, y FECHA DE VUELO.
      * ``` bash
        historical_delay_ratio_SIGLADES       float64
        historical_delay_ratio_OPERA          float64
        historical_delay_ratio_MES            float64
        historical_delay_ratio_periodo_dia    float64
        Last 1 Months_delay_ratio_OPERA       float64
        Last 1 Months_delay_ratio_DIA         float64
        Last 3 Months_delay_ratio_DIA         float64
        ```
        
2. Creacion de Docker container:
      * Maquina ubuntu slim buster con python 3.8.13
      * Instalacion de requerimientos y dependencias.
      * Copiar archivos necesarios para el despliegue.
      * Exponer puerto 8080 (Usualmente disponible en Google Cloud)
      * Iniciar servicio con uvicorn
       
        ``` bash
        # Use the official Python image as the base image
        FROM python:3.8.13-slim-buster

        # Set the working directory
        WORKDIR /main

        # Copy the requirements file to the working directory
        COPY requirements.txt .

        # Install the required packages
        RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
        RUN apt-get -y install curl
        RUN apt-get install libgomp1
        RUN pip install --no-cache-dir -r requirements.txt

        # Copy the app files to the working directory
        COPY main.py .
        COPY model/lgbm_model_late_flight_v1.pkl model/
        COPY model/lgbm_model_late_flight_v1.txt model/
        COPY utils/ utils/

        EXPOSE 8080

        # Start the app using the uvicorn server
        CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
        
        ```
3. Para efectos de deployment se utilizará Google Cloud Run, Google Cloud Build, Container Registry debido a su facil instalación, facil integración con github para CI/CD y bajo costo.

      * Los pasos para realizar esta accion son:
      * 1. Installing Cloud CLI:
      * 2. Create project
      * 3. Create service account
      * 4. Check Service Account created:
            ``` bash
            gcloud iam service-accounts list --project neuralworks-challenge
            ```
      * 5. Crear key para descargar localmente (y luego mover a GitHub)
            ``` bash
            gcloud iam service-accounts keys create ./keys.json --iam-account key-neuralworks-challenge@neuralworks-challenge.iam.gserviceaccount.com
            ```
      * 6. Activar service account localmente
            ``` bash
            gcloud auth activate-service-account --key-file=keys.json
            ```
      * 7. Build Docker image in Container Registry
            ``` bash
            gcloud builds submit --tag gcr.io/neuralworks-challenge/build-and-deploy-late-flight-model --project neuralworks-challenge 
            ```
      * 8. Run
            ``` bash
            gcloud run deploy build-and-deploy-late-flight-model --image gcr.io/neuralworks-challenge/build-and-deploy-late-flight-model --platform managed --project neuralworks-challenge --allow-unauthenticated --region us-east1 
            ```
      * 9. Configurar CI/CD desde github
      * 10. Prueba de aplicativo. (Para efectos del desafio la API admite llamadas sin autenticacion)
      * Documentacion: [Swagger Docs:](https://build-and-deploy-late-flight-model-5btddo6ama-ue.a.run.app//docs)

      * Esta APP contiene dos metodos para ser consumid. A continuacion se dejan adjuntos para su uso:
      
      * Metodo GET:
      
      * Endpoint: https://build-and-deploy-late-flight-model-5btddo6ama-ue.a.run.app/model_status
      * Response: 
      * ``` bash 
         {
          "python version": "3.8.13",
          "model_status": "Modelo activo y cargado 🔥",
          "model_type": "LGBM",
          "model_file": "lgbm_model_late_flight_v1.txt",
          "model_input_variables": [
            "OPERA",
            "SIGLADES",
            "FECHA_PROGRAMADA"
          ],
          "input_example": {
            "OPERA": "Sky Airline",
            "SIGLADES": "Calama",
            "FECHA_PROGRAMADA": "2017-11-27 13:00:00"
          }
        } 
        ```
      * Metodo POST:
      * Endpoint: https://build-and-deploy-late-flight-model-5btddo6ama-ue.a.run.app/predict_delay_probability
      * Headers:
      *     Content-Type: application/json
      * Input example: 
      * ``` bash 
        {
        "OPERA": "Sky Airline", 
        "SIGLADES": "Calama", 
        "FECHA_PROGRAMADA": "2017-11-27 13:00:00"
        }
        ```
      * Response: 
      * ``` bash
        {
        "delay_probability": 0.14,
        "clase": ["Baja probabilidad de atraso"]
        }
        ```
4. Pruebas de stress del servicio:
      * Para cumplir con la prueba de estres, se utiliza [wrk](https://github.com/wg/wrk) generando durante 45 segundos 50.000 requests a [endpoint](https://build-and-deploy-late-flight-model-5btddo6ama-ue.a.run.app/model_status)
      * 
      
6. Creacion de aplicacion backoffice en low code Budibase:
      * Link para uso: [neuralworks delay flight predictions on budibase](https://jaimearroyodevs.budibase.app/app/neuralworks-delay-flight-predictions)
      * Uso:
      * 1. Ingresa al link adjunto.
      * 2. Selecciona del listado un id de vuelo (fueron generados junto a data para efectos de datos (desde archivo testing) y prediccion)
      * 3. La app se encuentra integrada con API REST para hacer request cuando asi se solicite.
      * 4. Una vez seleccionado, hara un request al metodo predictions y traera la probabilidad de atraso.
      * Aplicacion:
      * ![image](https://user-images.githubusercontent.com/41343847/229156441-09de6488-210f-451a-9c90-c3dd2dd9cf35.png)





