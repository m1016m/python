import csv
from io import open

 
# open file
with open('AQI_20180717105825.csv', 'rb')as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        if int(row['AQI']) <=10:
         
           print str(row['County']).decode('string_escape')#解決list印出亂碼的問題