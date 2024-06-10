import requests


BASE_URL = 'https://swapi.dev/api/'

class SWAPIService:
    @staticmethod
    def fetch_data_by_id(endpoint, id):
        response = requests.get(f"{BASE_URL}{endpoint}/{id}/")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def fetch_data_by_url(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    @staticmethod
    def fetch_all_data(endpoint, id_page):
        url = (f"{BASE_URL}{endpoint}/")
        if int(id_page) > 1:
            url += f"?page={id_page}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
