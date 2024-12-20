# import folium
# from folium.plugins import HeatMap
# import pandas as pd
# import streamlit as st
# from scripts.language_utils import get_text
# from scripts.data_handler import STATION_COORDINATES
#
#
# def get_aqi_color(aqi):
#     """Return color based on AQI value"""
#     if aqi <= 50:
#         return 'green'
#     elif aqi <= 100:
#         return 'yellow'
#     elif aqi <= 150:
#         return 'orange'
#     elif aqi <= 200:
#         return 'red'
#     elif aqi <= 300:
#         return 'purple'
#     else:
#         return 'darkred'
#
#
# def create_aqi_heatmap(current_data):
#     """
#     Creates a dynamic AQI heatmap for Mexican AQI stations using the current data
#     """
#     if not current_data:
#         return folium.Map(location=[23.6345, -102.5528], zoom_start=5)
#
#     # Convert to list if single station data
#     if not isinstance(current_data, list):
#         current_data = [current_data]
#
#     # Create DataFrame with all stations data
#     df_data = []
#     for station_data in current_data:
#         station_name = station_data['AQI_STATION'].strip()  # Normalize station name
#         coords = STATION_COORDINATES.get(station_name)
#
#         if coords is None:
#             print(f"Warning: No coordinates found for station: {station_name}")
#             continue  # Skip this station if coordinates are not found
#
#         df_data.append({
#             'Station': station_name,
#             'Lat': coords['lat'],
#             'Lon': coords['lon'],
#             'AQI': station_data['AQI']
#         })
#
#     df = pd.DataFrame(df_data)
#
#     # Initialize map centered on the average location of stations
#     m = folium.Map(
#         location=[19.4326, -99.1332],  # Default center of Mexico
#         zoom_start=8,  # Initial zoom level
#         min_zoom=2,
#         max_zoom=10,
#         width='100%',
#         height='100%'  # Make the map fill the entire page
#     )
#
#     # Prepare heatmap data
#     heatmap_data = [[row['Lat'], row['Lon'], row['AQI']] for _, row in df.iterrows()]
#
#     # Add heatmap layer
#     HeatMap(
#         heatmap_data,
#         min_opacity=0.5,
#         max_val=200,
#         radius=50,
#         blur=35,
#         gradient={
#             0.0: 'green',
#             0.4: 'yellow',
#             0.6: 'orange',
#             0.8: 'red',
#             1.0: 'purple'
#         }
#     ).add_to(m)
#
#     # Add markers for each station
#     for _, row in df.iterrows():
#         station_data = next(d for d in current_data if d['AQI_STATION'] == row['Station'])
#         # Create popup content
#         lang = st.session_state.language
#         popup_content = f"""
#         <div style='font-family: Arial; font-size: 14px;'>
#             <b>{get_text(row['Station'], lang)}</b><br>
#             AQI: {row['AQI']}<br>
#             PM2.5: {station_data['PM_2.5']:.1f} µg/m³<br>
#             PM10: {station_data['PM_10']:.1f} µg/m³<br>
#             NO2: {station_data['NO2']:.1f} µg/m³<br>
#             SO2: {station_data['SO2']:.1f} µg/m³<br>
#             CO: {station_data['CO']:.1f} µg/m³<br>
#             O3: {station_data['O3']:.1f} µg/m³<br>
#             Traffic: {station_data['TRAFFIC_CONGESTION_INDEX']:.2f}
#         </div>
#         """
#
#         # Add marker with color based on AQI
#         folium.CircleMarker(
#             location=[row['Lat'], row['Lon']],
#             radius=8,
#             popup=folium.Popup(popup_content, max_width=250),
#             color=get_aqi_color(row['AQI']),
#             fill=True,
#             fill_color=get_aqi_color(row['AQI']),
#             fill_opacity=0.7,
#             weight=2
#         ).add_to(m)
#
#         # Add station label
#         folium.map.Marker(
#             [row['Lat'], row['Lon']],
#             icon=folium.DivIcon(
#                 html=f'<div style="font-size: 10pt; color: black;">{get_text(row["Station"], lang)}</div>'
#             )
#         ).add_to(m)
#
#     # Fit the map to the bounds of the markers
#     if not df.empty:
#         bounds = [[row['Lat'], row['Lon']] for _, row in df.iterrows()]
#         m.fit_bounds(bounds)
#
#     # Add legend
#     legend_html = """
#     <div style="position: fixed;
#                 bottom: 50px; right: 50px;
#                 border:2px solid grey; z-index:9999; font-size:14px;
#                 background-color: white;
#                 padding: 10px;
#                 opacity: 0.8;">
#         <p><strong>AQI Legend</strong></p>
#         <p><span style='color: green;'>■</span> 0-50: Good</p>
#         <p><span style='color: yellow;'>■</span> 51-100: Moderate</p>
#         <p><span style='color: orange;'>■</span> 101-150: Unhealthy for Sensitive Groups</p>
#         <p><span style='color: red;'>■</span> 151-200: Unhealthy</p>
#         <p><span style='color: purple;'>■</span> 201-300: Very Unhealthy</p>
#         <p><span style='color: darkred;'>■</span> 300+: Hazardous</p>
#     </div>
#     """
#     m.get_root().html.add_child(folium.Element(legend_html))
#
#     return m
#
import folium
from folium.plugins import HeatMap
import pandas as pd
import streamlit as st
from scripts.language_utils import get_text
from scripts.data_handler import STATION_COORDINATES


def get_aqi_color(aqi):
    """Return color based on AQI value for marker icons."""
    if aqi <= 50:
        return 'green'
    elif aqi <= 100:
        return 'blue'
    elif aqi <= 150:
        return 'orange'
    elif aqi <= 200:
        return 'red'
    elif aqi <= 300:
        return 'purple'
    else:
        return 'darkred'


def create_aqi_heatmap(current_data):
    """
    Creates a dynamic AQI heatmap with custom markers for Mexican AQI stations using the current data.
    """
    if not current_data:
        return folium.Map(location=[23.6345, -102.5528], zoom_start=5)

    # Convert to list if single station data
    if not isinstance(current_data, list):
        current_data = [current_data]

    # Create DataFrame with all stations data
    df_data = []
    for station_data in current_data:
        station_name = station_data['AQI_STATION'].strip()  # Normalize station name
        coords = STATION_COORDINATES.get(station_name)

        if coords is None:
            print(f"Warning: No coordinates found for station: {station_name}")
            continue  # Skip this station if coordinates are not found

        df_data.append({
            'Station': station_name,
            'Lat': coords['lat'],
            'Lon': coords['lon'],
            'AQI': station_data['AQI']
        })

    df = pd.DataFrame(df_data)

    # Initialize map centered on the average location of stations
    m = folium.Map(
        location=[19.4326, -99.1332],  # Default center of Mexico
        zoom_start=10,  # Initial zoom level
        min_zoom=2,
        max_zoom=20,
        width='100%',
        height='100%'  # Make the map fill the entire page
    )

    # Prepare heatmap data
    heatmap_data = [[row['Lat'], row['Lon'], row['AQI']] for _, row in df.iterrows()]

    # Add heatmap layer
    HeatMap(
        heatmap_data,
        min_opacity=0.5,
        max_val=200,
        radius=50,
        blur=35,
        gradient={
            0.0: 'green',
            0.4: 'yellow',
            0.6: 'orange',
            0.8: 'red',
            1.0: 'purple'
        }
    ).add_to(m)

    # Add custom markers for each station
    for _, row in df.iterrows():
        lang = st.session_state.language
        popup_content = f"""
        <div style='font-family: Arial; font-size: 14px;'>
            <b>{get_text(row['Station'], lang)}</b><br>
            AQI: {row['AQI']}
        </div>
        """

        # Add marker with custom icon based on AQI value
        icon_color = get_aqi_color(row['AQI'])
        folium.Marker(
            location=[row['Lat'], row['Lon']],
            popup=folium.Popup(popup_content, max_width=250),
            icon=folium.Icon(color=icon_color, icon="info-sign")
        ).add_to(m)

    # Fit the map to the bounds of the markers
    if not df.empty:
        bounds = [[row['Lat'], row['Lon']] for _, row in df.iterrows()]
        m.fit_bounds(bounds)

    # Add legend
    legend_html = """
    <div style="position: fixed;
                bottom: 50px; right: 50px;
                border:2px solid grey; z-index:9999; font-size:14px;
                background-color: white;
                padding: 10px;
                opacity: 0.8;">
        <p><strong>AQI Legend</strong></p>
        <p><span style='color: green;'>■</span> 0-50: Good</p>
        <p><span style='color: blue;'>■</span> 51-100: Moderate</p>
        <p><span style='color: orange;'>■</span> 101-150: Unhealthy for Sensitive Groups</p>
        <p><span style='color: red;'>■</span> 151-200: Unhealthy</p>
        <p><span style='color: purple;'>■</span> 201-300: Very Unhealthy</p>
        <p><span style='color: darkred;'>■</span> 300+: Hazardous</p>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    return m
