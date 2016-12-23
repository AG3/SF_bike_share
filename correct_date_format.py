import sqlite3

dbConn = sqlite3.connect('./data/yearThree.sqlite')
cursor = dbConn.cursor()

cursor.execute('SELECT * FROM trip')

trip = cursor.fetchall()
ind = 0

def correct_date(rawdate):
	sp = rawdate.split('/')
	if len(sp[0]) == 1:
		sp[0]='0'+sp[0]
	if len(sp[1]) == 1:
		sp[1]='0'+sp[1]
	res = sp[2]+'-'+sp[0]+'-'+sp[1]
	return res

#cursor.execute('PRAGMA synchronize = OFF')
#cursor.execute('PRAGMA jorunal_mode = OFF')
#cursor.execute('begin')
for i in trip:
	ind+=1
	sp1 = i[2].split(' ')
	date = correct_date(sp1[0])
	res1 = date+' '+sp1[1]

	sp1 = i[5].split(' ')
	date = correct_date(sp1[0])
	res2 = date+' '+sp1[1]#time already corrected
	'''
	t = sp1[1]
	#print(t)
	sp2 = t.split(':')
	h = sp2[0]
	m = sp2[1]
	if len(h)==1:
		h='0'+h
	sDate=t1+' '+h+':'+m

	sp1 = i[5].split(' ')
	t1 = sp1[0]
	t = sp1[1]
	sp2 = t.split(':')
	h = sp2[0]
	m = sp2[1]
	if len(h)==1:
		h='0'+h
	eDate=t1+' '+h+':'+m'''

	exe = 'UPDATE trip SET start_date=\''+res1+'\''+',end_date=\''+res2+'\''+' WHERE trip_id='+str(i[0])

	cursor.execute(exe)
	if ind % 1000 == 0:
		print(ind)
#cursor.execute('end')
dbConn.commit()
