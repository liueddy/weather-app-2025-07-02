import requests

class FetchWeather():
    """Wrapper to get weather from the OpenWeatherMap API.
    fields:
    - city
    - units
    - api_key
    - url
    methods:
    - __init__(str,str)     - initialise params for query
    - _validate_city(str)   - cast city to api-accepted string, does NOT check if valid
    - _validate_units(str)  - cast units is valid string, defaults to "standard" if invalid
    - _format_reponse(dict) - format API's JSON response in different format
    - fetch()               - calls API and returns JSON, if possible
    """
    def __init__(self,city:str,units:str="standard"):
        # type check given params
        self.city = self._validate_city(city)
        self.units = self._validate_units(units)
        self.api_key = "51feb6438334e6502cf871203e59a9af"
        self.url  = "https://api.openweathermap.org/data/2.5/weather?"
        self.url += f"q={self.city}&appid={self.api_key}&units={self.units}"

    def _validate_city(self,city:str) -> str:
        return str(city).strip().replace(" ","+")
    
    def _validate_units(self,units:str) -> str:
        u = str(units).strip().lower()
        if u == "metric" or u == "imperial":
            return u
        else:
            return "standard"

    def _format_response(self,rjson:dict) -> dict:
        pjson = {}
        try:
            pjson["city"] = rjson["name"]
            pjson["country"] = rjson["sys"]["country"]
            pjson["temperature"] = rjson["main"]["temp"]
            pjson["real_feel"] = rjson["main"]["feels_like"]
            pjson["weather"] = rjson["weather"][0]["description"]
            pjson["wind_spd"] = rjson["wind"]["speed"]
            pjson["units"] = self.units
        except:
            pjson["message"] = "city not found"
        finally:
            return pjson
        
    def fetch(self) -> dict:
        """Validates units, calls API,
        and returns a status code and a
        formatted JSON, if possible, 
        in the format:
            {'city': 'Toronto',
            'country': 'CA',
            'temperature': 25.17,
            'real_feel': 25.34,
            'weather': 'clear sky',
            'wind_spd': 6.71,
            'units': 'metric'}
        """
        res = requests.get(self.url)
        # res.json = self._format_response(res.json())

        return {"status_code":res.status_code, 
                "data": self._format_response(res.json())}

if __name__ == '__main__':
    foo = FetchWeather("fnwoinwe","metric")
    print(foo.fetch())