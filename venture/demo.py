import requests

r = requests.get(url='https://www.thecolorapi.com/id?hex=FFFF00')

print(r.status_code)

print(r.json())