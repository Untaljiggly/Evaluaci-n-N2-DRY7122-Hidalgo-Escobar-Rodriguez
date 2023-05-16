import requests
import urllib

api_url = "https://www.mapquestapi.com/directions/v2/route?"
key = "O9XcXatLu8978vP1u7C1JmgytEMxLCae"



while True:
    origin = input("Ingresa el punto de origen Crack: ")
    if origin == 'q':
        break
    destination = input ("Ingresa el destino rey: ")
    if destination == 'q':
        break
    url = api_url + urllib.parse.urlencode ({"key":key, "from": origin, "to":destination})
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"] * 1.61
        print("===================================================") 
        print(f"Informacion del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
        print(f"Duración total del viaje uwu: {trip_duration}.")
        print("Distancia en Kílometros mi chan: " + str("{:.2f}".format(distance) + " Kílometros recorridos uwu"))
    