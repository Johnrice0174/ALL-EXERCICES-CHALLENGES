# # dans le venv : pip install requests
# # dans le python shell :
#
# import requests
# import json
# from pprint import pprint
#
# url = "https://fr.dofus.dofapi.fr/classes"
# headers = {'Accept': "application/json"}
# response = requests.request("GET", url, headers=headers)
# # response.text
# data = response.json()
# pprint(data[0])
# print(data[0]["name"])

import requests, json

url = "https://fr.dofus.dofapi.fr/classes"
headers = {'Accept': "application/json"}
response = requests.request("GET", "https://fr.dofus.dofapi.fr/classes", headers=headers)
data = response.json()

for perso in data:
    print(perso["_id"])
    print(perso["name"])
    print(str(perso["roles"]))
    print(perso["description"])
    print(perso["maleImg"])
    print(perso["femaleImg"])
    print("\n--------------\n")
