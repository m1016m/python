import csv
with open('menu.csv', 'w', encoding='utf-8-sig') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['品名', '價格'])
    filewriter.writerow(['餛飩麵', '50'])
    filewriter.writerow(['蛋花湯', '25'])
    filewriter.writerow(['可樂', '20'])