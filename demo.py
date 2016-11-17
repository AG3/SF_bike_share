import sqlite3
import matplotlib.pyplot as plt

dbConn = sqlite3.connect('./database.sqlite')
cursor = dbConn.cursor()

cursor.execute("""
SELECT s.lat start_lat,
       s.long start_long,
       e.lat end_lat,
       e.long end_long,
       COUNT(DISTINCT t.Id) num_trips
FROM trip t
INNER JOIN station s ON t.start_station_id=s.id 
INNER JOIN station e ON t.end_station_id=e.id
WHERE s.city='San Francisco'
  AND e.city='San Francisco'
GROUP BY s.lat, s.long, e.lat, e.long""")
trip = cursor.fetchall()

print len(trip)

cursor.execute("SELECT * FROM station WHERE city='San Francisco'")
stations = cursor.fetchall()
print len(stations)

for i in stations:
	plt.scatter(i[3],i[2])#To match the real world location

maxTrip = max(map(lambda x: x[4], trip))
print maxTrip
for i in trip:
	plt.plot([i[1],i[3]],[i[0],i[2]],alpha=(i[4]*1.0/maxTrip),color="b")

plt.show()