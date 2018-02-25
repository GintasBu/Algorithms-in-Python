import pickle 
import bisect

D=pickle.load(open('PA61.p', 'rb'))

L=D.values()
Ls=sorted(L)

R={}
for i in Ls:
	j1=-i-10000
	j2=10000-i
	k1=bisect.bisect_left(Ls, j1)
	k2=bisect.bisect(Ls, j2)
	for l in Ls[k1:k2]:
		if i+l<=10000: 
			if i+l>=-10000:
				if i!=l:
					if i<l:
						R[(i,l)]=i+l
					else:
						R[(l,i)]=i+l



Rl=R.values()
Rl.sort()

RR={}
for z in Rl:
	if z not in RR:
		RR[z]=1
print len(RR)