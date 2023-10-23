# En exploitant l’API mise en place (station_information.json), affichez le nom de toutes les stations avec leur capacité actuelle

import json, requests

def get_station_names():
    response = requests.get("https://gbfs.citibikenyc.com/gbfs/fr/station_information.json")
    stations = json.loads(response.content)["data"]["stations"]
    return {station["name"]: station["capacity"] for station in stations}

stations = get_station_names()
for station_name, capacity in stations.items():
    print(f"{station_name}: {capacity}")
