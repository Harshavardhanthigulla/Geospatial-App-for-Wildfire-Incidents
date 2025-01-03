import streamlit as st
import folium
from streamlit_folium import st_folium
from fetch_data import fetch_wildfire_data
from streamlit.components.v1 import html

try:
    st.set_page_config(page_title="Wildfire Incident Tracker", layout="wide")
except AttributeError:
    pass

st.title("Wildfire Incidents in California")

col1, col2 = st.columns([1, 1])

with col1:
    data = fetch_wildfire_data()
    wildfire_incidents = data.get('features', [])
    st.write(f"Number of wildfire incidents: {len(wildfire_incidents)}")

    m = folium.Map(location=[37.7749, -122.4194], zoom_start=6)

    if wildfire_incidents:
        for incident in wildfire_incidents:
            properties = incident.get('attributes', {})
            geometry = incident.get('geometry', {})

            if 'rings' in geometry and len(geometry['rings']) > 0:
                longitude = geometry['rings'][0][0][0]
                latitude = geometry['rings'][0][0][1]

                name = properties.get('OBJECTID', 'Unknown')
                location = properties.get('POOCounty', 'Unknown')
                containment = properties.get('Containment', 'Unknown')
                size = properties.get('GISAcres', 'Unknown')

                popup_html = f"""
                <b>Incident ID:</b> {name if name else 'Unknown'}<br>
                <b>County:</b> {location if location else 'Unknown'}<br>
                <b>Containment:</b> {containment if containment else 'Unknown'}%<br>
                <b>Size:</b> {size if size else 'Unknown'} acres
                """

                folium.Marker(
                    location=[latitude, longitude],
                    popup=folium.Popup(popup_html, max_width=300)
                ).add_to(m)
    else:
        st.write("No data available")
    map_output = st_folium(m, width=700, height=500)

with col2:
    custom_html = """
    <style>
        .description {
            font-family: Arial, sans-serif;
            padding: 10px;
            border-radius: 8px;
        }
    </style>

    <div class="description">
        <h3>About the Tracker</h3>
        <p>This Wildfire Incident Tracker allows you to explore and track the most recent wildfire incidents happening in California. This app provides detailed information about each wildfire, including its name, location, containment status, and size.</p>
    </div>
    """

    st.markdown(custom_html, unsafe_allow_html=True)

footer_html = """
<div style="font-family: Arial, sans-serif; text-align: center; padding: 10px; background-color: #333; color: white; position: fixed; left: 0; bottom: 0; width: 100%;">
    <p>Powered by Streamlit, Folium, and NASA's Disaster Mapping Data</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
