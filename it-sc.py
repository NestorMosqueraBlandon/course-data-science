import requests
import pandas as pd

# Definir la URL base y otros parámetros
base_url = "https://century21mexico.com/v/resultados/operacion_venta/"
params = {"json": "true"}

# Lista para almacenar todos los resultados
all_results = []

# Hacer la solicitud GET para las primeras 16 páginas
for page_number in range(1, 16):
    if page_number > 1:
        url = base_url + "pagina_" + str(page_number)
    else:
        url = base_url
    response = requests.get(url, params=params)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = response.json()
        
        # Extraer los resultados de esta página y agregarlos a la lista
        results = data.get("results", [])
        all_results.extend(results)
        print("Página {} obtenida con éxito.".format(page_number))
    else:
        print("Error al obtener la página {}:".format(page_number), response.status_code)

# Convertir la lista de resultados en un DataFrame de pandas
df = pd.DataFrame(all_results)

# Guardar los datos en un archivo Excel
df.to_excel("resultados_casas_terrenos_departamentos.xlsx", index=False)
print("Datos guardados exitosamente en 'resultados_casas_terrenos_departamentos.xlsx'")
