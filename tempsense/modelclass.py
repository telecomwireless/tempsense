class TempSenseModel:

    latitude  = '35.125879'
    longitude = '-89.943262'

    def __init__(self, timestamp, room_temp, room_humid, current_temp, outside_humid):
        self.timestamp = timestamp
        self.room_temp = room_temp
        self.room_humid = room_humid
        self.current_temp = current_temp
        self.outside_humid = outside_humid
        self.sensor_err = False
        self.api_err = False