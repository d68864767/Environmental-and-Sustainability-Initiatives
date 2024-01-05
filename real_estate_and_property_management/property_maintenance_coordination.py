```python
import requests

class PropertyMaintenanceCoordination:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_maintenance_requests(self, property_id):
        response = requests.get(f'{self.base_url}/maintenance?property_id={property_id}')
        response.raise_for_status()
        return response.json()

    def get_maintenance_request_details(self, request_id):
        response = requests.get(f'{self.base_url}/maintenance/{request_id}')
        response.raise_for_status()
        return response.json()

    def create_new_maintenance_request(self, property_id, maintenance_details):
        response = requests.post(f'{self.base_url}/maintenance', params={'property_id': property_id}, json=maintenance_details)
        response.raise_for_status()
        return response.json()

    def update_maintenance_request(self, request_id, updated_details):
        response = requests.put(f'{self.base_url}/maintenance/{request_id}', json=updated_details)
        response.raise_for_status()
        return response.json()

    def delete_maintenance_request(self, request_id):
        response = requests.delete(f'{self.base_url}/maintenance/{request_id}')
        response.raise_for_status()
        return response.status_code
```
