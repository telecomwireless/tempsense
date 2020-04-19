import Adafruit_DHT
from modelclass import TempSenseModel
from datetime import datetime
from datetime import time
import logging

class ReadSensorData:

   sensor_logger = logging.getLogger(__name__)
   sensor_logger.setLevel(logging.WARNING)
   log_file_config = logging.FileHandler('/home/pi/tempSense/logs/logfile.log')
   formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
   log_file_config.setFormatter(formatter)
   sensor_logger.addHandler(log_file_config)
   sensor_model=Adafruit_DHT.DHT11
   gpio=17

   def gather_sensor_data(self):
       sensor_temp = ''
       sensor_humid = ''
       sensor_err = False
       time_stamp = ''
       try:
           room_humid, room_temp = Adafruit_DHT.read_retry(ReadSensorData.sensor_model, ReadSensorData.gpio)
           if room_humid is not None and room_temp is not None:
                sensor_temp = room_temp
                sensor_humid = room_humid
                time_stamp = str(datetime.now().replace(microsecond=0))
           else:
              ReadSensorData.sensor_logger.error("Couldn't get readings from sensor")
              sensor_err = True
              sensor_temp = "null"
              sensor_humid = "null"
              time_stamp = "null"
       except TimeoutError:
            ReadSensorData.sensor_logger.exception("can't get data from sensor")
       return (time_stamp,str(sensor_temp),str(sensor_humid),str(sensor_err))