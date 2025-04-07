import requests
from endpoint.base_endpoint import Endpoint


class GetAllObjects(Endpoint):
    GET_ALL_ENTITIES = "/getAll"

    def get_all_entities(self):
        self.response = requests.get(f"{self.URL}{self.GET_ALL_ENTITIES}")
        self.response_json = self.response.json().get('entity')

    def check_validate_response(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)