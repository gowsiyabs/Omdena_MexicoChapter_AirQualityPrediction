import streamlit as st
from Dashboard_pages import page_1, page_2
from scripts.language_utils import get_text
from scripts.data_handler import get_current_hour_data, get_all_stations
from datetime import datetime

# Configure the Streamlit page
st.set_page_config(
    page_title="Mexico AQI Monitor",
    page_icon="🌎",
    layout="wide",
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .stMetric {
        background-color: rgba(28, 131, 225, 0.1);
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .dataframe {
        background-color: rgba(28, 131, 225, 0.1);
        border-radius: 8px;
        padding: 10px;
    }
    div[data-testid="stMetricValue"] {
        font-size: 24px;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 16px;
    }
    section[data-testid="stSidebar"] {
        background-color: #262730;
        padding: 1rem;
    }
    section[data-testid="stSidebar"] > div {
        padding-top: 1rem;
    }
    .stRadio > label {
        font-size: 16px;
        padding: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)


def initialize_session_state():
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    if 'last_update' not in st.session_state:
        st.session_state.last_update = datetime.now()
    if 'current_data' not in st.session_state:
        st.session_state.current_data = get_current_hour_data()
    if 'selected_station' not in st.session_state:
        st.session_state.selected_station = 'All Stations'  # Default value


def main():
    initialize_session_state()

    # Sidebar
    with st.sidebar:
        # Title with emoji
        st.title("🌍 Mexico AQI Monitor")
        st.markdown("---")

        # Language selector
        st.subheader("🌐 Language / Idioma")
        lang_col1, lang_col2 = st.columns(2)
        with lang_col1:
            if st.button("English", use_container_width=True,
                         type="primary" if st.session_state.language == 'en' else "secondary"):
                st.session_state.language = 'en'
        with lang_col2:
            if st.button("Español", use_container_width=True,
                         type="primary" if st.session_state.language == 'es' else "secondary"):
                st.session_state.language = 'es'

        st.markdown("---")

        # Station selector

        st.subheader("📍 " + get_text('select_station', st.session_state.language))
        stations = ['All Stations'] + get_all_stations()
        selected = st.selectbox(
            "",
            options=stations,
            index=stations.index(st.session_state.selected_station),
            format_func=lambda x: get_text(x, st.session_state.language),
            label_visibility="collapsed"
        )

        if selected != st.session_state.selected_station:
            st.session_state.selected_station = selected
            st.rerun()

        st.markdown("---")
        # Page selector
        st.subheader("📊 " + get_text('select_page', st.session_state.language))
        page = st.radio(
            "",
            options=[get_text('page1', st.session_state.language),
                     get_text('page2', st.session_state.language)],
            label_visibility="collapsed"
        )

        # Information section
        st.markdown("---")
        st.markdown("### ℹ️ About")
        if st.session_state.language == 'en':
            st.markdown("""
                This dashboard shows real-time Air Quality Index (AQI) data
                for major AQI stations in Mexico. Data updates based on hourly readings.

                Made with ❤️ for Mexico
            """)
        else:
            st.markdown("""
                Este panel muestra datos del Índice de Calidad del Aire (AQI)
                en tiempo real para las principales estaciones de AQI en México.
                Los datos se actualizan según las lecturas por hora.

                Hecho con ❤️ para México
            """)

        # Last update time
        st.markdown("---")
        st.caption(f"Last update: {st.session_state.last_update.strftime('%Y-%m-%d %H:%M')}")

    # Update data if needed (every hour)
    current_hour = datetime.now().hour
    if current_hour != st.session_state.last_update.hour:
        st.session_state.current_data = get_current_hour_data()
        st.session_state.last_update = datetime.now()

    # Main content
    if page == get_text('page1', st.session_state.language):
        page_1.show()
    else:
        page_2.show()


if __name__ == "__main__":
    main()



