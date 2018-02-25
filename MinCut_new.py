import random
def randContr(D):
    if len(D)<3: 
        return D
    else: 
        a1=random.choice(D.keys())
        l1=D[a1]
        a2=random.choice(l1)
        l2=D[a2]
        l2=filter(lambda a: a!=a1, l2); 
        l1=filter(lambda a: a!=a2, l1); 
        D[a1]=l1+l2
        del D[a2]
        for i in D.values():
            for j in range(len(i)):
                if i[j]==a2: i[j]=a1
        randContr(D)
        return D 

		
		def getdata():
    data=open('KargerMinCut.txt', 'r')
    #data=open('test5.txt', 'r')
    D0={}
    for line in data:
        numb=line.split()
        if len(numb)>1:
            D0[numb[0]]=numb[1:]
    data.close()
    return D0

import copy

def many_cuts(D0):
    L={}
    k0=0
    for k in range(50):
        D=copy.deepcopy(D0)
        ans=randContr(D)
        L[len(ans.values()[0])]=[ans.keys()[0]]+[ans.keys()[1]]
        if k/1000>k0: 
            k0+=1
            print k
    return L

    #print D
##ll=min(L.keys())
#print L.keys()
#print ll

#print L[ll]


