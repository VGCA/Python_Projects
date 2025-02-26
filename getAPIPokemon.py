# importing the requests library
import requests

# api-endpoint
URL = "https://pokeapi.co/api/v2/pokemon"

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()
print('First twenty Pokemon ->')
for i in data['results']:
    print("Name: "+i['name'])
