import pytz
from datetime import datetime

argTimezone = pytz.timezone("America/Argentina/Buenos_Aires")
argDate = datetime.now(argTimezone)
print("Buenos Aires: " + argDate.strftime("%d/%m/%Y, %H:%M:%S"))