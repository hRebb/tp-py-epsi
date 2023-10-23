
# En exploitant l’API mise en place (station_status.json), affichez :
#  Le nombre de vélos électriques
#  Le nombre de vélos classiques
#  Le ratio de vélos électriques
import json, requests

def get_bikes():
    response = requests.get("https://gbfs.citibikenyc.com/gbfs/fr/station_status.json")
    data = json.loads(response.content)
    stations = data['data']['stations']
    num_ebikes = 0
    num_bikes = 0
    for station in stations:
        if 'num_ebikes_available' in station:
            num_ebikes += station['num_ebikes_available']
        if 'num_bikes_available' in station:
            num_bikes += station['num_bikes_available']
    ratio_ebikes = num_ebikes / (num_ebikes + num_bikes)
    print(f"Ratio de vélos électriques : {ratio_ebikes}")

print(get_bikes())