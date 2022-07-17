import fxcmpy
import datetime
import time
from csv import writer


#TODO: Set these: _________________ [ONLY FOR MINUTES, CREATE THE EMPTY FILES FIRST IN THE FOLDERS]
pairs = ["EUR/USD"] # Set the list of pairs you want to download
StartTime = 1492117200 # Set Start Time
EndTime = 1523653200 # Set End Time
token = "9c867df8c6a642a24a21ccd83db7368ff67a12fa"
con = fxcmpy.fxcmpy(access_token = token, server = 'demo')


def dataAdderr(timings, value, all_data):
    count = 0
    for i in timings:
        i = datetime.datetime.combine(i.date(), i.time())
        all_data.append({'time': (time.mktime(i.timetuple())), 'volume': value[count]['tickqty'], 'askopen': value[count]['askopen'], 'bidopen': value[count]['bidopen'], 'askhigh': value[count]['askhigh'], 'bidhigh': value[count]['bidhigh'], 'asklow': value[count]['asklow'], 'bidlow': value[count]['bidlow'], 'askclose': value[count]['askclose'], 'bidclose': value[count]['bidclose']})
        count += 1


lst_time = []
while EndTime-StartTime > 3600:
    lst_time.append([StartTime, StartTime+(620*24*3600)])
    StartTime = StartTime+(620*24*3600)+3600
lst_time[-1][-1] = EndTime

for currency in pairs:
    all_data = []
    for i in lst_time:
        data = con.get_candles(currency, period='H1', start=datetime.datetime.fromtimestamp(i[0]), end=datetime.datetime.fromtimestamp(i[1]))
        value = list(data.to_dict('index').values())
        timings = list(data.to_dict('index').keys())
        dataAdderr(timings, value, all_data)
    print('Writing on csv file')
    print(len(all_data))
    with open('Data/FXCM/' +currency.split('/')[0]+currency.split('/')[1]+ '.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for i in all_data:
            csv_writer.writerow([i['time'], i['volume'], i['askopen'], i['askhigh'], i['bidopen'], i['askhigh'], i['bidhigh'], i['asklow'], i['bidlow'], i['askclose'], i['bidclose']])
con.close()
