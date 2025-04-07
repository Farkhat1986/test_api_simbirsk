import requests
from endpoint.base_endpoint import Endpoint


class UpdateObject(Endpoint):
    PATCH_UPDATE_ENTITY = "/patch"

    def update_entity_by_id(self, obj_id, payload):
        self.response = requests.patch(f"{self.URL}{self.PATCH_UPDATE_ENTITY}/{obj_id}", json=payload)
        self.response_txt = self.response.text

    def check_type_response(self):
        assert isinstance(self.response_txt, str), "Не текстовое значение ответа сервиса"
        assert isinstance(int(self.response_txt), int), "Не числовой id в ответе сервиса"