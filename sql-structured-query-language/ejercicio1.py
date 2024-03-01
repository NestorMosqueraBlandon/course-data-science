import psycopg2 as pg
import pandas as pd
import numpy as np

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

query_insert = """
INSERT INTO air_quality (id, location, date, pollutant, concentration)
VALUES
    (1, 'Ciudad A', '2023-01-01', 'PM10', 25.5),
    (2, 'Ciudad A', '2023-01-01', 'NO2', 10.2),
    (3, 'Ciudad B', '2023-01-01', 'PM10', 18.7),
    (4, 'Ciudad B', '2023-01-01', 'NO2', 8.9),
    (5, 'Ciudad A', '2023-01-01', 'PM10', 28.3),
    (6, 'Ciudad A', '2023-01-01', 'NO2', 11.5),
    (7, 'Ciudad B', '2023-01-01', 'PM10', 20.1),
    (8, 'Ciudad B', '2023-01-01', 'NO2', 9.8) 
"""

query_delete_register = "DELETE FROM air_quality WHERE id=4"

query_group = " SELECT * FROM air_quality "
cursor.execute(query_group)

data = cursor.fetchall()
#connection.commit()

df = pd.DataFrame(data, columns=["id", "location", "date", "pollutant", "concentration"])

print(df)

df_mean = df["concentration"].mean()
df_dest = df["concentration"].std()
df_min = df["concentration"].min()
df_max = df["concentration"].max()


df_group = df.groupby("location")

print(df_group["concentration"].mean())

print("Media: ", df_mean)
print("Desviación Estandar: ", df_dest)
print("Mínimo: ", df_min)
print("Maximo: ", df_max)



