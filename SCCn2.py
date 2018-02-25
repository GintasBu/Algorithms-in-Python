# read data for SCC dict has numeric vertex labels
import datetime
print datetime.datetime.now().time()
data=open('scc.txt', 'rb')
D={}
t=0
Dr={} # reversed
for line in data:
	t+=1
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
		if t%50000==0:
			print t
		
import pickle

data.close()
pickle.dump(D, open("Dx.p", "wb"))
pickle.dump(Dr, open("Drx.p", "wb"))
print datetime.datetime.now().time()
print len(D), len(Dr)
