import sqlite3
import matplotlib.pyplot as plt
import datetime as DT

dbConn = sqlite3.connect('./database.sqlite')
cursor = dbConn.cursor()

cursor.execute('SELECT * FROM trip')

trip = cursor.fetchall()

for i in trip:
	t=i[2].split(' ')[0]
	t1=i[2].split(' ')[1]
	y = t.split('/')[2]
	m = t.split('/')[0]
	d = t.split('/')[1]
	if len(m)==1:
		m='0'+m
	if len(d)==1:
		d='0'+d
	sDate=y+'-'+m+'-'+d+' '+t1

	t=i[5].split(' ')[0]
	t1=i[5].split(' ')[1]
	y = t.split('/')[2]
	m = t.split('/')[0]
	d = t.split('/')[1]
	if len(m)==1:
		m='0'+m
	if len(d)==1:
		d='0'+d
	eDate=y+'-'+m+'-'+d+' '+t1

	exe = 'UPDATE trip SET start_date=\''+sDate+'\',end_date=\''+eDate+'\' WHERE id='+str(i[0])

	cursor.execute(exe)

dbConn.commit()
