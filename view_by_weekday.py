import matplotlib.pyplot as plt

ifile = open('./weekday_tripCount','r')

ofiles = []
daysCount = []
for i in range(0,7):
	ofiles.append(open('./single_'+str(i)+'_tripCount','w'))
	daysCount.append(0)

for line in ifile:
	t = line.split(' ')
	i = int(t[0])
	ofiles[i].write(str(daysCount[i])+' '+t[1])
	daysCount[i]+=1