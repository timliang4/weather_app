import requests

class Model:
    def __init__(self):
        self.unwanted_keys = ['last_updated_epoch', 'temp_c', 'is_day', 'wind_kph', 'wind_degree', 'wind_dir', 'pressure_mb', 
                              'condition', 'pressure_in', 'precip_mm', 'feeelslike_c', 'vis_km', 'gust_mph', 'gust_kph', 
                              'feelslike_c']
        self.keys_toNames = {'last_updated': 'Last Updated', "temp_f": "Temperature (Farenheit)", "wind_mph": "Wind (Mph)",
                             "precip_in": "Precipitation (Inches)", "humidity": "Humditiy", "cloud": "Cloudiness", 
                             "feelslike_f": "Feels like (Farneheit)", "vis_miles": "Visibility (Miles)", "uv": "UV Index"}
        
    def filter_function(self, pair):
        key,_ = pair
        if key in self.unwanted_keys:
            return False
        else:
            return True

    def _get_weather_data(self, location):
        url = "http://api.weatherapi.com/v1/current.json?"\
                    "key=73fdef3f975249a4923183253233004&"\
                    f"q={location}"
        response = requests.get(url)
        weather_data = response.json()

        if 'error' in weather_data.keys():
            return 'error: location not found'

        weather_data = dict(filter(self.filter_function, weather_data['current'].items()))
        result = {}
        for k, v in weather_data.items(): 
            result.update({self.keys_toNames[k]: weather_data[k]})
        return result
