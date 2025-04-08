from pydantic import BaseModel
from typing import Optional, Any

class Endpoint:
    URL = "http://localhost:8080"
    response = None
    response_model: Optional[BaseModel] = None

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code