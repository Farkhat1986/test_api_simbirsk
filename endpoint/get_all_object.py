import requests
from pydantic import BaseModel
from endpoint.base_endpoint import Endpoint
from schemas.entity import EntityResponse


class GetAllObjects(Endpoint):
    GET_ALL_ENTITIES = "/getAll"

    def get_all_entities(self) -> BaseModel | None:
        self.response = requests.get(f"{self.URL}{self.GET_ALL_ENTITIES}")
        response_data = self.response.json()

        if isinstance(response_data.get('entity'), list):
            self.response_model = [EntityResponse.model_validate(item) for item in response_data['entity']]
        else:
            self.response_model = [EntityResponse.model_validate(response_data['entity'])]

        return self.response_model