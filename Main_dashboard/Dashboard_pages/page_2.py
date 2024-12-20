import streamlit as st
from streamlit_folium import folium_static
from scripts.map_helpers import create_aqi_heatmap
from scripts.language_utils import get_text
from scripts.data_handler import get_current_hour_data


def show():
    lang = st.session_state.language

    st.title(get_text('aqi_heatmap', lang))

    # Always get data for all stations for the map
    all_stations_data = get_current_hour_data('All Stations')

    # Create and display map with all stations data
    m = create_aqi_heatmap(all_stations_data)
    folium_static(m, width=1000, height=600)

    # Add refresh button
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button(get_text('refresh_map', lang)):
            # Get new data for all stations and update session state
            st.session_state.current_data = get_current_hour_data('All Stations')
            st.rerun()

