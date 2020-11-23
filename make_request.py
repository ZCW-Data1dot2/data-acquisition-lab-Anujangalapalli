import json
import requests


offset = 1
limit = 1000
i = range(0,40)
for k in i:
    response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?limit=1000&offset='+str(offset), headers={'Token':'Key'})
    j = json.loads(response.text)

    with open('locations_'+str(k)+'.json', 'w') as json_file:
         json.dump(j, json_file, indent=2)
    offset += limit
