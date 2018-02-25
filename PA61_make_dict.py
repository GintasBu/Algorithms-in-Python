import pickle
f=open('PA61.txt', 'rb')
D={}
D2={}
k=1
for i in f.readlines():
	D[k]=int(i)
	if int(i) not in D2:
		D2[k]=int(i)
	else:
		print i
	k+=1
f.close()

print len(D), len(D2)
pickle.dump(D, open("PA61.p", "wb"))				#make dict to serve as hashtable
pickle.dump(D2, open("PA61unique.p", "wb"))

	