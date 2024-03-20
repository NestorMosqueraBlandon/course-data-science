import requests
import pandas as pd

# Definir la URL del endpoint
url = "https://remax.com.mx/map/FetchMapData"

# Parámetros del formulario de datos
data = {
    "moneda": "MXN",
    "locationKeyword": "",
    "operacion": "1"
}

# Lista para almacenar todos los resultados
all_results = []

# Hacer la solicitud POST
response = requests.post(url, data=data)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    
    # Extraer los datos de la propiedad de los resultados y agregarlos a la lista
    prop_data = data.get("data", {}).get("prop_data", [])
    all_results.extend(prop_data)
    print("Datos obtenidos exitosamente.")
else:
    print("Error al hacer la solicitud:", response.status_code)

# Convertir la lista de resultados en un DataFrame de pandas
df = pd.DataFrame(all_results)

# Guardar los datos en un archivo Excel
df.to_excel("resultados_propiedades_remax.xlsx", index=False)
print("Datos guardados exitosamente en 'resultados_propiedades_remax.xlsx'")
