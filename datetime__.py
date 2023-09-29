from datetime import datetime
import pytz

def __datetime__():
    datetimeIndia = datetime.now(pytz.timezone('Asia/Kolkata'))
    datetimeFormat = datetimeIndia.strftime('%d:%m:%Y %H:%M:%S')
    return datetimeFormat
    
def __timestamp__():
    datetimeIndia = datetime.now(pytz.timezone('Asia/Kolkata'))
    seconds =(datetimeIndia.timestamp())
    nanoseconds = (seconds*1000000000)
    timestampFormat = round (nanoseconds)
    return timestampFormat

datetime__ = __datetime__()
print("datetime :", datetime__)

timestamp__ = __timestamp__()
print("Timestamp:", timestamp__)
