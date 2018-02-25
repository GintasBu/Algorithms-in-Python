# read data for SCC dict has numeric vertex labels
import datetime
print datetime.datetime.now().time()
data=open('scctest1.txt', 'r')
d=data.read()
data.close()
del data
l=d.rsplit('\n')
del d
D={}
Dl={}
Dr={} # reversed
Drl={}
for line in l:
	ll=line.split()
	if len(ll)>0:
		n=ll[1]
		n=int(n)
		n0=ll[0]
		n0=int(n0)
		if n0 in D.keys():
			D[n0].append(n)
		else:
			D[n0]=[n]
		if n not in D.keys(): D[n]=[]

		if n in Dr.keys():
			Dr[n].append(n0)
		else:
			Dr[n]=[n0]
		if n0 not in Dr.keys(): Dr[n0]=[]
		
import pickle
#json.dump(D, file("D.json", 'w'))
#json.dump(Dr, file("Dr.json", 'w'))
#dD=open('D.txt', 'w')
#dD.write(D)
#dD.close()
pickle.dump(D, open("Dtest.p", "wb"))
pickle.dump(Dr, open("Drtest.p", "wb"))
print datetime.datetime.now().time()
print len(D), len(Dr)
print D, Dr
#print D
#print "reversed"
#print Dr