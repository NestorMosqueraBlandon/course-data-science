# Motor de base de datos todas basadas en SQL
"""
MySQL
PostgreSQL
SQLite
Oracle Database
Microsoft SQL Server
IBM Db2
MariaDB
"""

# Ahora vamos a usar PostgreSQL
import psycopg2 as pg
import pandas as pd
# Establecer conexion a la Base de Datos
#postgres://username:password@host/databasename

# connection = pg.connect(
#     dbname="",
#     user="",
#     password="",
#     host="",
#     post=5432
# )

connection = pg.connect("postgr953918.us-east-2.aws.neon.tech/neondb")

# Crear un cursor para ejecutar las consultas SQL
cursor = connection.cursor()

# Ejecutar una consulta
#cursor.execute(" SELECT * FROM users ")
#projects = cursor.fetchall()

#df_projects = pd.DataFrame(projects)
#print(df_projects)


#cursor.execute(" SELECT name, born_date, gender FROM users ")
#users = cursor.fetchall()

#df_users = pd.DataFrame(users)
#print(df_users)

#cursor.execute(" SELECT gender, COUNT(*) FROM users GROUP BY gender ")
#users = cursor.fetchall()

#df_users = pd.DataFrame(users)
#print(df_users)

cursor.execute(" SELECT COUNT(*) FROM users ")
users = cursor.fetchall()

df_users = pd.DataFrame(users)
print(df_users)