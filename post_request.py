import requests

# La URL de tu API (el servidor Flask que estás corriendo localmente)
url = 'http://127.0.0.1:5000/users'

# Haciendo una solicitud POST a la API
response = requests.post(url)

# Imprimir la respuesta de la API
print("Response Code:", response.status_code)
print("Response Body:", response.json())
