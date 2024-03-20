# 

import requests #Librería para hacer peticiones a enlaces o webs o apis
import pandas as pd

url = "https://www.metrocuadrado.com/rest-search/search?realEstateBusinessList=venta&realEstateStatusList=nuevo&from=0&size=50"

results = []

response = requests.get(url, headers={ "X-Amz-Cf-Id": "4Zhlppj9RD4YgbZ1yfLpM1Wd81r19oAhPmp9idtnneGkqgHsUdJhRg==" })

print(response)