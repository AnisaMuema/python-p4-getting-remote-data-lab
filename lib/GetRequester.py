import requests
import json

class GetRequester:
   
    def __init__(self, url):
        self.url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

    def get_response_body(self):
        requester = requests.get(self.url)
        return requester.content
        pass

    def load_json(self):
        loads = json.loads(self.get_response_body())
        return loads
        pass