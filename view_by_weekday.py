import sqlite3
import matplotlib.pyplot as plt

dbConn = sqlite3.connect('./database.sqlite')
cursor = dbConn.cursor()

f = open('weekday_tripCount','w')

for i in range(0,7):
	cursor.execute('SELECT * FROM trip WHERE strftime(\'%w\', start_date)=\''+str(i)+'\'')
	trip = cursor.fetchall()
	plt.bar(i,len(trip))
	f.write(str(i)+' '+str(len(trip)))
plt.show()
f.close()