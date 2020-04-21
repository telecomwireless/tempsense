import csv
from datetime import date, timedelta
import shutil
from modelclass import TempSenseModel
import logging
from weatherapi import WeatherAPI
from sensordata import ReadSensorData
import time

class FileProcessor:

    today_date = date.today()
    tomorrow_date = today_date +  timedelta(1)
    fieldname = ['TimeStamp', 'RoomTemp', 'RoomHumid', 'SensorErr', 'CurrentTemp', 'OutsideTemp',  'APIErr', 'Latitude', 'Longitude']
    file_logger = logging.getLogger(__name__)
    file_logger.setLevel(logging.WARNING)
    log_file_config = logging.FileHandler('/home/pi/tempSense/logs/logfile.log')
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    log_file_config.setFormatter(formatter)
    file_logger.addHandler(log_file_config)
    counter = 0

    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
        self.rotate_loc = '/mnt/mydisk/temphum/'
        self.full_file_path = self.file_path+"/"+self.file_name+"-"+str(date.today())+".csv"

    def write_to_csv(self, sensor_tuple, weather_tuple):
            header_write = self.rotate_files()            
            with open(self.full_file_path, mode='a+') as file:
                 writer = csv.DictWriter(file, FileProcessor.fieldname, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                 if header_write or FileProcessor.counter == 0:
                     FileProcessor.counter += 1
                     writer.writeheader()
                        
                 writer.writerow({'TimeStamp':sensor_tuple[0],'RoomTemp':sensor_tuple[1], 'RoomHumid': sensor_tuple[2], 
                 'SensorErr': sensor_tuple[3], 'CurrentTemp': weather_tuple[0], 'OutsideTemp': weather_tuple[1],
                 'APIErr': weather_tuple[2], 'Latitude': TempSenseModel.latitude, 'Longitude' : TempSenseModel.longitude })

    def read_from_csv(self):
        pass

    def rotate_files(self):
        ''' This method will move files to the external mount connected to the PI '''
        my_var = False
        if FileProcessor.today_date < date.today():
            shutil.move(self.full_file_path, self.rotate_loc)
            FileProcessor.today_date = date.today()
            my_var = True
            time.sleep(240)
        return my_var
