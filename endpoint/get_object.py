import requests
from endpoint.base_endpoint import Endpoint


class GetObject(Endpoint):
    GET_ENTITY = "/get"

    def get_entity_by_id(self, object_id):
        self.response = requests.get(f"{self.URL}{self.GET_ENTITY}/{object_id}")
        self.response_json = self.response.json()

    def check_validate_response(self, schema):
        schema.model_validate(self.response_json)