class Endpoint:
    URL = "http://localhost:8080"
    response = None
    response_json = None
    response_txt = None

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code