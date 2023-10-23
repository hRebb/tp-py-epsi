# En exploitant l’API mise en place (station_status.json), affichez :
#  Le nombre de stations en service (active)
#  Le nombre de stations HS (out_of_service)
#  Le ratio de stations en service

import json, requests

def get_station_status():
    response = requests.get("https://gbfs.citibikenyc.com/gbfs/fr/station_status.json")
    data = json.loads(response.content)
    stations = data['data']['stations']
    num_active = 0
    num_out_of_service = 0
    for station in stations:
        if 'status' in station and station['status'] == 'active':
            num_active += 1
        elif 'status' in station and station['status'] == 'out_of_service':
            num_out_of_service += 1
    ratio_active = num_active / len(stations)
    return num_active, num_out_of_service, ratio_active

print(get_station_status())