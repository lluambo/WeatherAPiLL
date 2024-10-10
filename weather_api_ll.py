import requests #Used to get the json info from the API
class City: #Class to get the data from the API and blueprint of what info we need for a city
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):#Method to get the data from the API
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&{API key}")#Put your API key from https://openweathermap.org here
        except:
            print("No internet access :(")
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):#Method to print the data
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In {self.name} it is currently {self.temp}{units_symbol}")
        print(f"Today's High: {self.temp_max}{units_symbol}")
        print(f"Today's Low: {self.temp_min}{units_symbol}")

my_city = City("Nairobi", -1.286389, 36.8219, units="metric")#test cases
my_city.temp_print()#test cases

vacation_city = City("Wroclaw", 51.1093, 17.0385, units="imperial")#test cases
my_city.temp_print()#test cases
