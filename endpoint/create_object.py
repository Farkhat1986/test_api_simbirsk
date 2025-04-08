import requests
from pydantic import BaseModel
from endpoint.base_endpoint import Endpoint
from schemas.entity import EntityResponse

class CreateObject(Endpoint):
    POST_CREATE_ENTITY = "/create"

    def create_entity(self, payload: dict) -> BaseModel | None:
        self.response = requests.post(f"{self.URL}{self.POST_CREATE_ENTITY}", json=payload)
        self.response_model = EntityResponse.model_validate(self.response.json())
        return self.response_model