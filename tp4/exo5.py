# Citi Bike est le système de vélos en libre-service de la ville de New York. Une API est disponible, permettant d’obtenir des informations en temps réel : 
# https://gbfs.citibikenyc.com/gbfs/fr/station_information.json
# https://gbfs.citibikenyc.com/gbfs/fr/station_status.json

# Nous souhaitons trouver quelles sont les stations les plus éloignées. Pour cela, nous utiliserons la célèbre formule du théorème de Pythagore : c = √a2 + b2
# Trouvez l’algorithme permettant de trouver quelles sont les 2 stations les plus éloignées.

import math, requests

class Station:
    def __init__(self):
        self.url = "https://gbfs.citibikenyc.com/gbfs/fr/station_information.json"
        self.data = None

    def get_data(self):
        response = requests.get(self.url)
        self.data = response.json()['data']['stations']

    def get_distance(self):
        self.get_data()

        distance_max = 0
        station1 = ""
        station2 = ""
        station_names = []

        for station in self.data:
            station_names.append(station['name'])
            for station2 in self.data:
                distance = math.sqrt((station['lat'] - station2['lat'])**2 + (station['lon'] - station2['lon'])**2)
                if distance > distance_max:
                    distance_max = distance
                    station1 = station['name']
                    station2 = station2['name']

        return station_names, station1, station2, distance_max

station = Station()
station_names, station1, station2, distance_max = station.get_distance()
print(f"{station_names[0]}\n{station_names[1]}\n {distance_max:.2f}")