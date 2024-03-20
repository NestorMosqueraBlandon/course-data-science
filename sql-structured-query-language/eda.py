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

#EDA
#HISTOGRAMA DE DISTIRBUCIÓN

# plt.hist(df["concentration"], bins=100, color="skyblue", edgecolor="black")
# plt.xlabel("Variable")
# plt.ylabel("Frecuencia")
# plt.title("Histograma de Distirbución")
# plt.show()

#Diagrama de dispersión
plt.scatter(df["date"], df["concentration"], color="green")
plt.xlabel("Location")
plt.ylabel("Concentration")
plt.title("Histograma de Dispersión")
plt.show()

#Diagrama de Caja
# plt.boxplot(df["concentration"])
# plt.xlabel("Concentración")
# plt.ylabel("Valor")
# plt.title("Histograma de Caja")
# plt.show()

#Gráfico de Barras
# df["location"].value_counts().plot( kind="bar", color="orange")
# plt.xlabel("Location")
# plt.ylabel("Concentration")
# plt.title("Histograma de Dispersión")
# plt.show()

# df["date"] = pd.to_datetime(df["date"])

# plt.plot(df["date"], df["concentration"], color="red")
# plt.xlabel("Fecha")
# plt.ylabel("Concentration")
# plt.title("Anánlisis Temporal")
# plt.show()