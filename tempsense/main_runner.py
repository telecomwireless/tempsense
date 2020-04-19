''' This is the main script that should be used to run this project  '''

from modelclass import TempSenseModel
from weatherapi import WeatherAPI
from sensordata import ReadSensorData
from filehandler import FileProcessor
import time

sensor_read = ReadSensorData()
weather_read = WeatherAPI()
filer = FileProcessor('temp','/home/pi/tempSense')
while True:
        sensor_tup = sensor_read.gather_sensor_data()
        weather_tup = weather_read.call_api()
        filer.write_to_csv(sensor_tup,weather_tup)
        time.sleep(180)
        


