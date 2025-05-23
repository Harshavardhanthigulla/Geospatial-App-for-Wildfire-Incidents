# Geospatial-Data-App
This Streamlit application fetches wildfire incident data from the California Natural Resources Agency and displays it on an interactive map. Users can click on markers to view detailed information about individual wildfire incidents.

## Tools and Technologies

- **Python**: Backend development
- **Streamlit**: Web framework
- **Folium**: Geospatial visualization library
- **Requests**: API data fetching

## Data Source

- **Endpoint**: https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Interagency_Perimeters_YearToDate/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json
- **Description**: Wildfire incident data for the past month in California.

## Setup Instructions

1. Install the required packages:
    ```
    pip install streamlit folium requests streamlit_folium
    ```

2. Run the app:
    ```
    streamlit run app.py
    ```
## File Structure:

- `app.py`: Main application file that sets up the Streamlit app and renders the interactive map.
- `fetch_data.py`: Script to fetch wildfire incident data from the API endpoint.

## Functionality

1. **Backend Development**:
    - Fetches wildfire incident data from the provided endpoint.
    - Processes and serves the data to the frontend.

2. **Frontend Development**:
    - Creates an interactive map using Folium.
    - Places markers for each wildfire incident showing the location on the map.
    - Allows users to click on markers to view details about each wildfire (e.g., fire name, location, containment status, size).
  

## App Screenshot

Here is what the interactive wildfire map looks like:

![image](https://github.com/user-attachments/assets/62c95b6f-9da5-4245-9ebe-3af2f85e6214)


## Justification for Framework Choices

I chose Streamlit for its simplicity and speed in building data-driven apps with minimal code. It seamlessly integrates with Python libraries like Folium for mapping and Requests for fetching data. Unlike Flask or Django, Streamlit combines both the backend and frontend, automating server-client communication. This eliminates the need to create custom frontend components or integrate JavaScript frameworks, making the development process faster and less complex. Folium provides an easy way to create interactive maps, and Streamlit handles everything in one tool, making it perfect for this project.

