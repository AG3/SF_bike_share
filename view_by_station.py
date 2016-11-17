import sqlite3
import matplotlib.pyplot as plt

dbConn = sqlite3.connect('./database.sqlite')
cursor = dbConn.cursor()

f = open('stationId_weekday_tripCount','w')

exe = 'SELECT station.id, station.name FROM station'

cursor.execute(exe)
staions = cursor.fetchall()

count = 7*len(staions)

for i in staions:
	for j in range(0,7):
		exe = 'SELECT COUNT(*) FROM trip WHERE trip.start_station_id=\''+str(i[0])+'\' AND strftime(\'%w\', trip.start_date)=\''+str(j)+'\''
		cursor.execute(exe)
		trip = cursor.fetchall()
		#print trip[0][0]
		f.write(str(i[0])+' '+str(j)+' '+str(trip[0][0])+'\n')
		count=count-1
		print str(count)+' stations left...'
f.close()