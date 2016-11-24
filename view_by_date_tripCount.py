import sqlite3

dbConn = sqlite3.connect('./data/database.sqlite')
cursor = dbConn.cursor()

exe = 'SELECT date(start_date),strftime(\'%w\',date(start_date)),count(*) FROM trip GROUP BY date(start_date)'

cursor.execute(exe)

trip = cursor.fetchall()

ofiles = []
daysCount = []
for i in range(0,7):
	ofiles.append(open('./single_'+str(i)+'_tripCount','w'))
	daysCount.append(0)

for t in trip:
	#t = line.split(' ')
	i = int(t[1])
	ofiles[i].write(t[0]+' '+str(t[2])+'\n')