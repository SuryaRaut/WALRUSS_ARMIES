import requests
from config import Q_C_API_KEY, SCANNED_HOST
from requests.exceptions import HTTPError, Timeout, RequestException

def get_scanned_host(api_keys: str = Q_C_API_KEY) -> list:
    headers = {
        "Accept": "application/json",
        "token": api_keys
    }
    try:
        res = requests.post(SCANNED_HOST, headers=headers, timeout=15)
        if res.status_code != 200:
            print(f"Error: {res.status_code}, Response: {res.content}")
            res.raise_for_status()
        
        data = res.json()
        hosts = data.get("hosts", [])
        
        if not isinstance(hosts, list):
            print(f"Unexpected data format: {data}")
            return []
        
        return hosts
    
    except HTTPError as httpErr:
        print(f"Http error encountered: {httpErr} - Status Code: {res.status_code}")
        raise
    except Timeout:
        print(f"Request timeout")
        raise
    except RequestException as reqErr:
        print(f"An error occurred with the request: {reqErr}")
        raise
    except ValueError:
        print(f"Failed to parse JSON response: {res.content}")
        raise
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        raise
