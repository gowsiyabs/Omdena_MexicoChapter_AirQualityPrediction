import streamlit as st
import pandas as pd
from scripts.language_utils import get_text
from scripts.data_handler import get_current_hour_data, get_all_stations

def get_aqi_color(aqi):
    if aqi <= 50:
        return "#00e400"  # Good
    elif aqi <= 100:
        return "#ffff00"  # Moderate
    elif aqi <= 150:
        return "#ff7e00"  # Unhealthy for Sensitive Groups
    elif aqi <= 200:
        return "#ff0000"  # Unhealthy
    elif aqi <= 300:
        return "#99004c"  # Very Unhealthy
    else:
        return "#7e0023"  # Hazardous

def get_aqi_status(aqi, lang):
    if aqi <= 50:
        return get_text('good', lang)
    elif aqi <= 100:
        return get_text('moderate', lang)
    elif aqi <= 150:
        return get_text('unhealthy_sensitive', lang)
    elif aqi <= 200:
        return get_text('unhealthy', lang)
    elif aqi <= 300:
        return get_text('very_unhealthy', lang)
    else:
        return get_text('hazardous', lang)

def show():
    lang = st.session_state.language

    # Get the selected station from the sidebar
    selected_station = st.session_state.selected_station

    # Get current data
    current_data = get_current_hour_data(selected_station)

    if not current_data:
        st.error("No data available")
        return

    # Handle single station or all stations
    if isinstance(current_data, list):
        # All stations mode
        stations_data = current_data
    else:
        # Single station mode
        stations_data = [current_data]

    # Main AQI Display
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title(get_text('current_aqi', lang))

        # Calculate average AQI for all stations or use single station AQI
        current_aqi = sum(station['AQI'] for station in stations_data) / len(stations_data)
        status = get_aqi_status(current_aqi, lang)

        display_title = ""
        if selected_station != 'All Stations':
            station_name = get_text(stations_data[0]['AQI_STATION'], lang)
            display_title = f"{station_name} - "

        st.markdown(
            f"""
            <div style='background-color: {get_aqi_color(current_aqi)}; 
                        padding: 20px; 
                        border-radius: 10px; 
                        text-align: center'>
                <h1 style='color: black'>{display_title}{int(current_aqi)} - {status}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Pollutant Levels
    st.subheader(get_text('pollutant_levels', lang))

    if selected_station == 'All Stations':
        # Calculate average pollutant levels
        pollutants = {
            'PM2.5': sum(station['PM_2.5'] for station in stations_data) / len(stations_data),
            'PM10': sum(station['PM_10'] for station in stations_data) / len(stations_data),
            'NO2': sum(station['NO2'] for station in stations_data) / len(stations_data),
            'SO2': sum(station['SO2'] for station in stations_data) / len(stations_data),
            'CO': sum(station['CO'] for station in stations_data) / len(stations_data),
            'O3': sum(station['O3'] for station in stations_data) / len(stations_data)
        }
    else:
        pollutants = {
            'PM2.5': stations_data[0]['PM_2.5'],
            'PM10': stations_data[0]['PM_10'],
            'NO2': stations_data[0]['NO2'],
            'SO2': stations_data[0]['SO2'],
            'CO': stations_data[0]['CO'],
            'O3': stations_data[0]['O3']
        }

    cols = st.columns(3)
    for idx, (pollutant, value) in enumerate(pollutants.items()):
        with cols[idx % 3]:
            st.metric(pollutant, f"{value:.1f} µg/m³")

    # Station Table
    st.subheader(get_text('station_aqi', lang))

    df = pd.DataFrame([{
        'Station': get_text(station['AQI_STATION'], lang),
        'AQI': station['AQI'],
        'Status': get_aqi_status(station['AQI'], lang),
        'Traffic_congestion_Index': station['TRAFFIC_CONGESTION_INDEX']
    } for station in stations_data])

    st.dataframe(df, use_container_width=True)