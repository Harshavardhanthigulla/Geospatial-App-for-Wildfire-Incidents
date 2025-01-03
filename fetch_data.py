import requests

def fetch_wildfire_data():
    url = "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Interagency_Perimeters_YearToDate/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        data = response.json()
         
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {}
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON response")
        return {}
