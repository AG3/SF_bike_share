import sqlite3

dbConn = sqlite3.connect('./data/database.sqlite')
cursor = dbConn.cursor()

exe = 'SELECT julianday(date(start_date)),count(*) FROM trip GROUP BY date(start_date)'

cursor.execute(exe)

trip = cursor.fetchall()

ofile = open('./days_tripCount','w')

for t in trip:
	#t = line.split(' ')
	i = int(t[1])
	ofile.write(str(int(t[0]))+' '+str(t[1])+'\n')