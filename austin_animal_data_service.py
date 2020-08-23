import json
import urllib.request, urllib.error

OUTCOME_URL = 'http://data.austintexas.gov/resource/9t4d-g238.json'


def get_animal_outcome_data():
    with open('assets/application_token') as f:
        app_token = f.read()

    headers = {'X-App-Token': app_token,
               'Accept': 'application/json'}
    try:
        request = urllib.request.Request(url=OUTCOME_URL, headers=headers)
        return json.loads(urllib.request.urlopen(request).read())

    except urllib.error.HTTPError as e:
        print(e)
