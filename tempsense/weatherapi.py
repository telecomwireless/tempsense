
import requests, json
from modelclass import TempSenseModel
import logging

class WeatherAPI:
#    https://api.openweathermap.org/data/2.5/weather?lat=35.12&lon=-89.94&units=imperial&appid=59a50d2b0a7f529c6700a33b51b1d3d9
   api_key = '59a50d2b0a7f529c6700a33b51b1d3d9'
   base_url = "https://api.openweathermap.org/data/2.5/weather?"
   weather_logger = logging.getLogger(__name__)
   weather_logger.setLevel(logging.WARNING)
   log_file_config = logging.FileHandler('/home/pi/tempSense/logs/logfile.log')
   formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
   log_file_config.setFormatter(formatter)
   weather_logger.addHandler(log_file_config)

   def call_api(self):
       full_url = WeatherAPI.base_url + "appid=" + WeatherAPI.api_key + "&lat=" + TempSenseModel.latitude + "&lon=" + TempSenseModel.longitude + "&units=imperial"
       temp = ''
       humid = ''
       api_err = False
       try:
           resp = requests.get(full_url).json()
       except requests.exceptions.Timeout:
           WeatherAPI.weather_logger.exception("Timeout requesting the open api weather")
           api_err = True         
       if resp["cod"] != 404:
           main_resp = resp["main"]
           temp = str(main_resp["temp"])
           humid = str(main_resp["humidity"])
       return (temp,humid, str(api_err))