# take out those record which virance is lower than the biggest one's 5%
# also can used to find those stable records

ifile = open('stationId_weekday_tripCount.txt','r')
ofile = open('stationId_weekday_tripCount.exclude_high_variance','w')

dc = 0
data = []
raw = []
avr = 0
maxRes = 0
while(1):
	s = ifile.readline()
	dc=dc+1
	if s=="":
		break
	num = s.split(' ')
	count = int(num[2])
	raw.append(s)
	data.append(count)
	avr=avr+count
	if dc == 7:
		t = 0
		for i in data:
			t=t+(i-avr)*(i-avr)
		res = t / 7
		
		res = res*1.0/369328122
		print res
		if res<=0.05:
			for i in raw:
				ofile.write(i)
		dc = 0
		data = []
		raw = []
		avr = 0