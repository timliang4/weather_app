import requests

class Model:
    def __init__(self):
        self.unwanted_keys = ['last_updated_epoch', 'temp_c', 'is_day', 'wind_kph', 'wind_degree', 'wind_dir', 'pressure_mb', 
                              'condition', 'pressure_in', 'precip_mm', 'feeelslike_c', 'vis_km', 'gust_mph', 'gust_kph']
        
    def filter_function(self, pair):
        key, value = pair
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
            return f'error: location not found'

        weather_data = dict(filter(self.filter_function, weather_data['current'].items()))
        output_string = ''
        for item in weather_data.items():
            output_string += f'{item[0]}: {item[1]}\n'
        return output_string
