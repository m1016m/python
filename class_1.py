
import csv
import re

fn = 'AQI_20180717105825.csv'

with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)
    print  " Row = " ,csvReader.line_num , str(listReport).decode('string_escape')#csvReader.line_num表示當前的行數
    for x in listReport:
        for y in x :
            if y[] <=10:
                print str(listReport['County']).decode('string_escape')#解決list印出亂碼的問題
            else:
                print "No Good"
            





 
    
