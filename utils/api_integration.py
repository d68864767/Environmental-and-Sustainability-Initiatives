```python
import requests
import json

def get_api_data(url, headers=None):
    """
    Fetch data from an API.
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

def post_api_data(url, data, headers=None):
    """
    Post data to an API.
    """
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

def put_api_data(url, data, headers=None):
    """
    Update data in an API.
    """
    try:
        response = requests.put(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

def delete_api_data(url, headers=None):
    """
    Delete data from an API.
    """
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None
```
