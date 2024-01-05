```python
import requests

class RealEstateMarketAnalysis:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_market_data(self, location):
        response = requests.get(f'{self.base_url}/market-data?location={location}')
        response.raise_for_status()
        return response.json()

    def get_property_market_value(self, property_id):
        response = requests.get(f'{self.base_url}/market-data/property-value/{property_id}')
        response.raise_for_status()
        return response.json()

    def get_rental_market_value(self, rental_id):
        response = requests.get(f'{self.base_url}/market-data/rental-value/{rental_id}')
        response.raise_for_status()
        return response.json()

    def get_market_trends(self, location, period):
        response = requests.get(f'{self.base_url}/market-data/trends?location={location}&period={period}')
        response.raise_for_status()
        return response.json()
```
