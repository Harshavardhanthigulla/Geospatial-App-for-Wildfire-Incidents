# -Geospatial-Data-App
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

1. Clone the repository:
    ```
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```
    pip install streamlit folium requests
    ```

4. Run the app:
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
