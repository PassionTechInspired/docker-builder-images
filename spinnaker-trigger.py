import os
import requests
import json

tag = os.environ['CI_COMMIT_SHORT_SHA']
project = os.environ['CI_PROJECT_NAME']
endpoint = os.environ['ENDPOINT']

print("Endpoint: " + endpoint)
print("Project: " + project)
print("Tag: " + tag)

body = json.dumps({
        "parameters": {
            "tag": tag,
            "project": project
        }
    })

r = requests.Session()
r.headers.update({'content-type': 'application/json'})

response = r.post(url=endpoint, data=body)

print("Response from Spinnaker:")
print(response.json())
