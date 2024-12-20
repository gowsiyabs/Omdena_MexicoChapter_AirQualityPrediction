import pandas as pd
from datetime import datetime
from pathlib import Path

# AQI station coordinates
# STATION_COORDINATES = {
#     'Ajusco Medio': {'lat': 19.272222222222, 'lon': -99.207777777778},
#     'Ajusco': {'lat': 19.204499182, 'lon': -99.254832314},
#     'Benito Juarez': {'lat': -19.371666666667, 'lon': -99.159166666667},
#     'Hospital General de México': {'lat': 20.9479, 'lon': -101.4258},
#     'Merced': {'lat': 19.424722222222, 'lon': -99.119722222222},
#     'Miguel Hidalgo': {'lat': -19.404, 'lon': -99.202722222222},
#     'Milpa Alta': {'lat': 19.1928, 'lon': -99.0238},
#     'Pedregal': {'lat': 19.325277777778, 'lon': -99.204166666667},
#     'San Agustin': {'lat': 19.533055555556, 'lon': -99.030555555556},
#     'Santa Fe': {'lat': 19.354431, 'lon': -99.259150},
#     'Tlalnepantla': {'lat': -19.529166666667, 'lon': -99.204722222222},
#     'UAM Iztapalapa': {'lat': -19.360833333333, 'lon': -99.07388888888899},
#     'Xalostoc': {'lat': -19.526111111110996, 'lon': -99.0825}
# }

STATION_COORDINATES = {
    'Ajusco Medio': {'lat': 19.272222222222, 'lon': -99.207777777778},
    'Ajusco': {'lat': 19.204499182, 'lon': -99.254832314},
    'Benito Juarez': {'lat': 19.371666666667, 'lon': -99.159166666667},
    'Hospital General de México': {'lat': 19.4135, 'lon': -99.149},
    'Merced': {'lat': 19.424722222222, 'lon': -99.119722222222},
    'Miguel Hidalgo': {'lat': 19.404, 'lon': -99.202722222222},
    'Milpa Alta': {'lat': 19.1928, 'lon': -99.0238},
    'Pedregal': {'lat': 19.325277777778, 'lon': -99.204166666667},
    'San Agustin': {'lat': 19.533055555556, 'lon': -99.030555555556},
    'Santa Fe': {'lat': 19.354375, 'lon': -99.25915},
    'Tlalnepantla': {'lat': 19.529166666667, 'lon': -99.204722222222},
    'UAM Iztapalapa': {'lat': 19.36, 'lon': -99.07},
    'Xalostoc': {'lat': 19.526111111111, 'lon': -99.0825}
}


def load_data(file_path='C:\\Users\\garla\\PycharmProjects\\Mexico_AQI\\Data\\AQI_dummy_data.xlsx'):
    """Load data from Excel file"""
    try:
        df = pd.read_excel(file_path)
        print(df.head())
        required_columns = [
            'AQI_STATION', 'HOUR_DAY', 'AQI', 'PM_2.5', 'PM_10',
            'NO2', 'SO2', 'CO', 'O3', 'TRAFFIC_CONGESTION_INDEX'
        ]
        missing_columns = set(required_columns) - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns in Excel file: {missing_columns}")
        return df
    except FileNotFoundError:
        print(f"Error: Data file not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def get_current_hour_data(station='All Stations'):
    """Get data for current hour of the day"""
    current_hour = datetime.now().hour
    df = load_data()
    
    if df is None or df.empty:
        return None
        
    # Filter data for the current hour
    current_data = df[df['HOUR_DAY'] == current_hour]
    
    if current_data.empty:
        return None

    # If specific station is selected
    if station != 'All Stations':
        station_data = current_data[current_data['AQI_STATION'] == station]
        if station_data.empty:
            return None
        return station_data.iloc[0].to_dict()
    
    # Return all stations data for the current hour
    return current_data.to_dict('records')

def get_station_coordinates(station_name):
    """Get coordinates for a specific station"""
    return STATION_COORDINATES.get(station_name)

def get_all_stations():
    """Get list of all station names"""
    return list(STATION_COORDINATES.keys())

def get_data_by_station(station_name):
    """Get all data for a specific station"""
    df = load_data()
    if df is None or df.empty:
        return None
    
    station_data = df[df['AQI_STATION'] == station_name]
    if station_data.empty:
        return None
        
    return station_data.iloc[0].to_dict()

def get_all_hours_data():
    """Get data for all hours"""
    df = load_data()
    if df is None or df.empty:
        return None
    
    return df.to_dict('records')
 