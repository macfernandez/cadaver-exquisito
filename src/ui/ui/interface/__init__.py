import requests


class Interface:
    def __init__(self):
        self.base_url = "http://localhost:8000"

    def post_chat(self, text: str) -> str:
        url = f"{self.base_url}/chat"
        response = requests.post(url, json={"text": text})
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")
        return response.json().get("text")
