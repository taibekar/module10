import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = '766497dcb329441ebec590728891014b'
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'
    incidents = []
    # /incidents/elevators, /incidents/escalators
  # use 'requests' to do a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL, headers= headers)

  # retrieve the JSON from the response
    data = response.json()

  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
    for incident in data['ElevatorIncidents']:

        # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
        #   -StationCode, StationName, UnitType, UnitName
        if incident['UnitType'] == unit_type.upper()[:-1]:
            temp_incident = {
                'StationCode': incident['StationCode'],
                'StationName': incident['StationName'],
                'UnitType': incident['UnitType'],
                'UnitName': incident['UnitName']
            }

            # add each incident dictionary object to the 'incidents' list
            incidents.append(temp_incident)
    # return the list of incident dictionaries using json.dumps()
    return json.dumps(incidents)


if __name__ == '__main__':
    app.run(debug=True)
