import os
import requests
import json

# Tool for getting IMOs, which are essential for other API calls

apikey = os.environ['secretapikey']
f = open('Project Shipnames.txt')
ship_names = f.readlines()

for line in ship_names:
  ship = line.rstrip()
  read_url = 'https://services.marinetraffic.com/api/shipsearch/%s/shipname:%s/protocol:jsono' %(apikey,ship)
  response = requests.get(read_url)
  json_data = json.loads(response.text)
  try:
    IMO = json_data[0]["IMO"]
    if IMO == '0':
      print("No IMO")
    else:
      print(IMO)
  except IndexError:
    print("API Exception")
