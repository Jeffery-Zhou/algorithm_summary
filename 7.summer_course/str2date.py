import time
import datetime

start =  datetime.datetime.strptime('20160720','%Y%m%d')
end = datetime.datetime.strptime('20160801','%Y%m%d')
days_num =  (end - start).days

date_lst = []

for i in range(0, days_num+1):
	delta = datetime.timedelta(days=i)
	date_lst.append((start+delta).strftime('%Y%m%d'))

print date_lst


 