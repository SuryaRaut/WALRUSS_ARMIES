import requests
from config import Q_C_API_KEY, QUALYS_API_URL
from requests.exceptions import HTTPError, Timeout, RequestException

def get_host_from_qualys(api_keys: str = Q_C_API_KEY) -> list:
    #print(f"Using API Key: {Q_C_API_KEY}")
    headers = {
        "Accept": "application/json",
        "token": api_keys
    }
    try:
        #set http call timeout 15 soconds
        res = requests.post(QUALYS_API_URL, headers=headers, timeout=15)
        if res.status_code != 200:
            print(f"Error: {res.status_code}, Response: {res.content}")
            res.raise_for_status()
        return res.json()
    
    #catch http errors   
    except HTTPError as httpErr:
        print(f"Http error encounterd: {httpErr} - Status Code: {res.status_code}")
        raise
    #catch timeout error
    except Timeout:
        print(f"Request timeout")
        raise
    #catch netowrk related error
    except RequestException as reqErr:
        print(f"An Error encountered : {reqErr}")
        raise
    #catch json parse error
    except ValueError:
        print(f"Failed to parse Json response: {res.content}")
        raise
    #catch other exception
    except Exception as ex:
        print(f"An Unexpected error encountered: {ex}")
        raise