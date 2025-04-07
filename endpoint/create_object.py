import requests
from endpoint.base_endpoint import Endpoint


class CreateObject(Endpoint):
    POST_CREATE_ENTITY = "/create"

    def create_entity(self, payload):
        self.response = requests.post(f"{self.URL}{self.POST_CREATE_ENTITY}", json=payload)
        self.response_txt = self.response.text

    def check_type_response(self):
        assert isinstance(self.response_txt, str), "Не текстовое значение ответа сервиса"
        assert isinstance(int(self.response_txt), int), "Не числовой id в ответе сервиса"