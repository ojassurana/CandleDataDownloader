# FORMAT: t,v,o,h,l,c

import requests
from csv import writer


pairs = ['DOGE/USDT'] # The pairs
seconds = 3600  # The number of seconds in each block (for e.g. 3600 for 1 hr time frame)
StartTime = 1653807600 # Starting time
EndTime = 1656486000    # Ending time
lst_time = []
while EndTime-StartTime > seconds:
    lst_time.append([StartTime, StartTime+seconds*1500])
    StartTime = StartTime+seconds*1500 + seconds
print(lst_time)    
lst_time[-1][-1] = EndTime
for currency in pairs:
    all_data = []
    for i in lst_time:
        data = requests.get('https://ftx.com/api/markets/'+currency+'/candles?resolution='+str(seconds)+'&start_time='+str(i[0])+'&end_time='+str(i[1])).json()['result']
        all_data = all_data + data
    print('writing')
    with open('Data/FTX/' +currency.split('/')[0]+currency.split('/')[1]+ '.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for i in all_data:
            csv_writer.writerow([i['time'], i['volume'], i['open'], i['high'], i['low'], i['close']])
