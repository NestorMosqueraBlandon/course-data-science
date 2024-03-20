import pandas as pd
import psycopg2 as pg
from datetime import datetime, timedelta
import re

# Conexión a la base de datos
conn_string = ""
connection = pg.connect(conn_string)
cursor = connection.cursor()

# Ejecutar la consulta SQL
query_qet_air_quality = "SELECT last_login FROM users"
cursor.execute(query_qet_air_quality)
data = cursor.fetchall()

# Crear DataFrame con la respuesta de la consulta
df = pd.DataFrame(data)

# Asignar nombres a las columnas
df.columns = ['last_login']

# Función para limpiar la cadena de fecha y hora
def clean_date_string(date_str):
    match = re.search(r'(\w+\s+\w+\s+\d+\s+\d{4}\s+\d+:\d+:\d+)', date_str)
    if match:
        return match.group(1)
    return None

# Limpiar la columna 'last_login'
df['last_login'] = df['last_login'].apply(clean_date_string)

# Convertir la columna 'last_login' a formato datetime
df['last_login'] = pd.to_datetime(df['last_login'], format='%a %b %d %Y %H:%M:%S')

# Obtener la fecha de hace un mes
ultimo_mes = datetime.now() - timedelta(days=30)

# Filtrar las filas para obtener las entradas que ocurrieron durante el último mes
usuarios_ultimo_mes = df[df['last_login'] >= ultimo_mes]

# Contar el número de usuarios únicos
usuarios_unicos_ultimo_mes = usuarios_ultimo_mes.shape[0]

# Imprimir el número de usuarios únicos que ingresaron durante el último mes
print("Usuarios que ingresaron durante el último mes:", usuarios_unicos_ultimo_mes)
