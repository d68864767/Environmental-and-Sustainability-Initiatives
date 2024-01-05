```python
import requests

class PropertyListingAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_property_listings(self, location):
        response = requests.get(f'{self.base_url}/listings?location={location}')
        response.raise_for_status()
        return response.json()

    def get_property_details(self, property_id):
        response = requests.get(f'{self.base_url}/listings/{property_id}')
        response.raise_for_status()
        return response.json()
```
