import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder #Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import psycopg2 as pg

#Traer la data desde la base de datos
                #Motor        #Username   #Password           #Host -> Server                                  #DBNAME
conn_string = "postgresql://rvehardware:wrQRPy7OVds9@ep-withered-snowflake-a54v41cn.us-east-2.aws.neon.tech/data-science"

connection = pg.connect(conn_string)
cursor = connection.cursor()

query_qet_air_quality = " SELECT * FROM air_quality "
cursor.execute(query_qet_air_quality)

data = cursor.fetchall()

#Tranformar la data
df = pd.DataFrame(data, columns=["ID", "location", "date", "pollutant", "concentration"])
#Revisar si hay valores nulos, duplicados, outliers, mal formateados

stats_by_location = df.groupby("location")["concentration"].agg([ "min", "max", "mean", "std" ])
print("Estadistica descriptiva: ", stats_by_location)

#Visualizar los datos
#El for es un ciclo
for location, datos in df.groupby("location"):
    plt.scatter(datos["date"], datos["concentration"], label=location)
    plt.xlabel("Date")
    plt.ylabel("Concentration")
    plt.title("Pollutant concentration by location")
    plt.legend()
    #plt.show()

X = pd.get_dummies(df[['location', 'pollutant']])
y = df["concentration"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=72)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nDesempeño del modelo:")
print("Error Cuadrático Medio (MSE):", mse)
print("Coeficiente de Determinación (R^2):", r2)


df_predict = pd.DataFrame({ "Real_concentration": y_test, "Predict_concentration": y_pred })

stats_predicts = df_predict.describe()
print(stats_predicts)

plt.scatter(y_test, y_pred)
plt.plot(y_test, y_test, color='red', linestyle='--')  # Línea de referencia: y_pred = y_test

plt.xlabel("Concentración Real")
plt.ylabel("Concentración Predicha")
plt.title("Predicciones de modelo vs. Datos Reales")
plt.show()