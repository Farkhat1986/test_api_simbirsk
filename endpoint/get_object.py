import requests
from pydantic import BaseModel
from endpoint.base_endpoint import Endpoint
from schemas.entity import EntityResponse

class GetObject(Endpoint):
    GET_ENTITY = "/get"

    def get_entity_by_id(self, object_id: int) -> BaseModel | None:
        self.response = requests.get(f"{self.URL}{self.GET_ENTITY}/{object_id}")
        self.response_model = EntityResponse.model_validate(self.response.json())
        return self.response_model