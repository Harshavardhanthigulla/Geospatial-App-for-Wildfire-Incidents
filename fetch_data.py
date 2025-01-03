import requests

def fetch_wildfire_data():
    url = "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Interagency_Perimeters_YearToDate/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    response = requests.get(url)
    
    print(response.text)  
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON response")
        data = {}
    
    return data
