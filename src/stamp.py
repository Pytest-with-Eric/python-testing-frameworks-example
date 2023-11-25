import time
from datetime import datetime

def timestamp_using_time():
    """
    Function to generate timestamp using time library
    """
    return time.time()

def timestamp_using_datetime():
    """
    Function to generate timestamp using datetime library
    """
    current_time = datetime.now()
    return current_time.timestamp()

def custom_timestamp(date_string):
    """
    Function to generate custom timestamp
    """
    dt_format = datetime.strptime(date_string, '%d.%m.%Y %H:%M:%S')
    return dt_format.timestamp()

def convert_timestamp(time_stamp):
    """
    Function to convert timestamp to normal date and time
    """
    return datetime.fromtimestamp(time_stamp)

