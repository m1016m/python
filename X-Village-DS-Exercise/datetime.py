import time
import datetime

 
def print_next_day() :
     today = datetime.date.today()
     print (today)
     tomorrow = today + datetime.timedelta(days=1)
     return tomorrow

print (print_next_day())
