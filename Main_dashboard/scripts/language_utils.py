def get_text(key, language):
    translations = {
        'nav_title': {
            'en': 'Mexico AQI Monitor',
            'es': 'Monitor de AQI de México'
        },
        'select_page': {
            'en': 'Select Page',
            'es': 'Seleccionar página'
        },
        'page1': {
            'en': 'AQI Overview',
            'es': 'Resumen de AQI'
        },
        'page2': {
            'en': 'AQI Heatmap',
            'es': 'Mapa de Calor AQI'
        },
        'current_aqi': {
            'en': 'Current Air Quality Index',
            'es': 'Índice de Calidad del Aire Actual'
        },
        'pollutant_levels': {
            'en': 'Pollutant Levels',
            'es': 'Niveles de Contaminantes'
        },
        'station_aqi': {
            'en': 'Station AQI Levels',
            'es': 'Niveles de AQI por Estación'
        },
        'refresh_map': {
            'en': 'Refresh Map',
            'es': 'Actualizar Mapa'
        },
        'aqi_heatmap': {
            'en': 'AQI Heatmap of Mexico Monitoring Stations',
            'es': 'Mapa de Calor AQI de Estaciones de Monitoreo'
        },
        # AQI Status translations
        'good': {
            'en': 'Good',
            'es': 'Bueno'
        },
        'moderate': {
            'en': 'Moderate',
            'es': 'Moderado'
        },
        'unhealthy_sensitive': {
            'en': 'Unhealthy for Sensitive Groups',
            'es': 'Poco saludable para grupos sensibles'
        },
        'unhealthy': {
            'en': 'Unhealthy',
            'es': 'Poco saludable'
        },
        'very_unhealthy': {
            'en': 'Very Unhealthy',
            'es': 'Muy poco saludable'
        },
        'hazardous': {
            'en': 'Hazardous',
            'es': 'Peligroso'
        },
        # Station translations
        'Ajusco Medio': {
            'en': 'Ajusco Medio',
            'es': 'Ajusco Medio'
        },
        'Ajusco': {
            'en': 'Ajusco',
            'es': 'Ajusco'
        },
        'Benito Juarez': {
            'en': 'Benito Juarez',
            'es': 'Benito Juárez'
        },
        'Hospital General': {
            'en': 'General Hospital',
            'es': 'Hospital General de México'
        },
        'Merced': {
            'en': 'Merced',
            'es': 'Merced'
        },
        'Miguel Hidalgo': {
            'en': 'Miguel Hidalgo',
            'es': 'Miguel Hidalgo'
        },
        'Milpa Alta': {
            'en': 'Milpa Alta',
            'es': 'Milpa Alta'
        },
        'Pedregal': {
            'en': 'Pedregal',
            'es': 'Pedregal'
        },
        'San Agustin': {
            'en': 'San Agustin',
            'es': 'San Agustín'
        },
        'Santa Fe': {
            'en': 'Santa Fe',
            'es': 'Santa Fe'
        },
        'Tlalnepantla': {
            'en': 'Tlalnepantla',
            'es': 'Tlalnepantla'
        },
        'UAM Iztapalapa': {
            'en': 'UAM Iztapalapa',
            'es': 'UAM Iztapalapa'
        },
        'Xalostoc': {
            'en': 'Xalostoc',
            'es': 'Xalostoc'
        },
        'select_station': {
            'en': 'Select Station',
            'es': 'Seleccionar Estación'
        },
        'All Stations': {
            'en': 'All Stations',
            'es': 'Todas las Estaciones'
        }
    }
    
    return translations.get(key, {}).get(language, key) 