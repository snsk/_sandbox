import requests
import yaml
import codecs
import json

with open('secret.yml', 'r') as yml:
    config = yaml.safe_load(yml)

headers = {'Authorization': 'Bearer {}'.format(config['api_key'])}
data = requests.get(
    'https://gihoz-api.veriserve.co.jp/api/v1/users/snsk/repositories/MyRepository/test_cases/180acbf7-56dc-498e-b880-bc94952c6e44'
    ,headers=headers
)
data_json = json.loads(data.text)
test_case_json = json.loads(data_json["data"]["attributes"]["test_case_json"])
print(json.dumps(test_case_json, indent=2))