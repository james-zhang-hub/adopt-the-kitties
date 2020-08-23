import json
import os
import urllib.request, urllib.error

APP_TOKEN = os.getenv('SOCRATA_APP_TOKEN')
OUTCOME_URL = os.getenv('AAC_OUTCOME_URL')


def get_animal_outcome_data():
    headers = {'X-App-Token': APP_TOKEN,
               'Accept': 'application/json'}
    try:
        request = urllib.request.Request(url=OUTCOME_URL, headers=headers)
        return json.loads(urllib.request.urlopen(request).read())

    except urllib.error.HTTPError as e:
        print(e)
