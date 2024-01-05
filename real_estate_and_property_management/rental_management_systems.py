```python
import requests

class RentalManagementSystem:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_rental_properties(self, location):
        response = requests.get(f'{self.base_url}/rentals?location={location}')
        response.raise_for_status()
        return response.json()

    def get_rental_details(self, rental_id):
        response = requests.get(f'{self.base_url}/rentals/{rental_id}')
        response.raise_for_status()
        return response.json()

    def create_new_rental(self, property_id, rental_details):
        response = requests.post(f'{self.base_url}/rentals', params={'property_id': property_id}, json=rental_details)
        response.raise_for_status()
        return response.json()

    def update_rental(self, rental_id, updated_details):
        response = requests.put(f'{self.base_url}/rentals/{rental_id}', json=updated_details)
        response.raise_for_status()
        return response.json()

    def delete_rental(self, rental_id):
        response = requests.delete(f'{self.base_url}/rentals/{rental_id}')
        response.raise_for_status()
        return response.status_code
```
