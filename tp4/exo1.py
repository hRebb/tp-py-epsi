# Citi Bike est le système de vélos en libre-service de la ville de New York. Une API est disponible, permettant d’obtenir des informations en temps réel : 
# https://gbfs.citibikenyc.com/gbfs/fr/station_information.json
# https://gbfs.citibikenyc.com/gbfs/fr/station_status.json
# Installez la lib Requests, qui vous permettra de faire des requêtes web afin d'interroger cette API.

import json, requests

def get_station_information():
    response = requests.get("https://gbfs.citibikenyc.com/gbfs/fr/station_information.json")
    return json.dumps(json.loads(response.content), indent=4)

print(get_station_information())