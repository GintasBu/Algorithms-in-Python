inputfile=open('PA11.txt',"rb");
#inputfile=open('test13.txt',"rb");
#import os
data=[(9999,9999,9999)]
for line in inputfile.readlines():
    line=line.strip()
    if len(line)>0:
        row=line.split(' ')
        row[0]=int(row[0])
        row[1]=int(row[1])
        data.append((row[0], row[1], float(row[0])/float(row[1])))
inputfile.close()
#print data
L=sorted(data, key=lambda x: (x[2], x[1]), reverse=True)[1:]
c=[] # completion times
wc=[] # weightet sum
#print L
for l in L:
	if len(c)==0:
		c.append(l[1])
		wc.append(l[1]*l[0])
	else:
		c.append(l[1]+c[len(c)-1])
		wc.append(c[len(c)-1]*l[0]+wc[len(wc)-1])
#print c, wc
print wc[9990:]