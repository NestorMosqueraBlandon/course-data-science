import psycopg2 as pg
import pandas as pd
import numpy as np
from datetime import datetime
import random

connection_string = "postgresql://rvehardware:wrQRPy7OVds9@ep-withered-snowflake-a54v41cn.us-east-2.aws.neon.tech/data-science"

connection = pg.connect(connection_string)

cursor = connection.cursor()

query = """
CREATE TABLE air_quality ( 
    id INT PRIMARY KEY,
    location VARCHAR(100),
    date DATE,
    pollutant VARCHAR(100),
    concentration FLOAT
)
"""

query_delete = "DROP TABLE air_quality"
ciudades = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena']

# Generación de 100 filas de datos
for i in range(1, 367):
    ciudad = random.choice(ciudades)
    fecha = datetime(2023, random.randint(1, 12), random.randint(1, 28)).strftime('%Y-%m-%d')
    pollutant = random.choice(['PM10', 'NO2'])
    concentration = random.uniform(0, 100)
    
    # Sentencia SQL para insertar datos
    query_insert = f"""
    INSERT INTO air_quality (id, location, date, pollutant, concentration)
    VALUES
        ({i}, '{ciudad}', '{fecha}', '{pollutant}', {concentration})
    """
    
    # Ejecutar la sentencia SQL
    cursor.execute(query_insert)

# Confirmar la transacción
#connection.commit()

query_delete_register = "DELETE FROM air_quality"

query_group = " SELECT * FROM air_quality "
#cursor.execute(query_delete_register)

#data = cursor.fetchall()
connection.commit()

#df = pd.DataFrame(data, columns=["id", "location", "date", "pollutant", "concentration"])

#print(df)

#df_mean = df["concentration"].mean()
#df_dest = df["concentration"].std()
#df_min = df["concentration"].min()
#df_max = df["concentration"].max()


#df_group = df.groupby("location")

#print(df_group["concentration"].mean())

#print("Media: ", df_mean)
#print("Desviación Estandar: ", df_dest)
#print("Mínimo: ", df_min)
#print("Maximo: ", df_max)



