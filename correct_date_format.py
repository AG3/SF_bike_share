import sqlite3
import matplotlib.pyplot as plt
import datetime as DT

dbConn = sqlite3.connect('./data/database.sqlite')
cursor = dbConn.cursor()

cursor.execute('SELECT * FROM trip')

trip = cursor.fetchall()

for i in trip:
	t1 = i[2].split(' ')[0]
	t = i[2].split(' ')[1]
	h = t.split(':')[0]
	m = t.split(':')[1]
	if len(h)==1:
		h='0'+h
	sDate=t1+' '+h+':'+m

	t1 = i[5].split(' ')[0]
	t = i[5].split(' ')[1]
	h = t.split(':')[0]
	m = t.split(':')[1]
	if len(h)==1:
		h='0'+h
	eDate=t1+' '+h+':'+m

	exe = 'UPDATE trip SET start_date=\''+sDate+'\''+',end_date=\''+eDate+'\''+' WHERE id='+str(i[0])

	cursor.execute(exe)

dbConn.commit()
