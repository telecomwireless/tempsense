from datetime import date
from datetime import datetime, timedelta
import time
#from tempsense.filehandler import FileProcessor
# t1 = datetime.now().replace(microsecond=0)
# time_stamp = ''
# time_stamp = str(datetime.now().replace(microsecond=0))
# print(time_stamp)

def my_decorator(func):
    def wrappe():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrappe

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()