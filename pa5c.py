import numpy as np
import copy 

def tsp3(items):
    N=int(items[0][0])
    dist=get_data_dict(items)
    sets1=create_setl(1, N, 1)
    
    A1=np.zeros([N,len(sets1)])+float('+inf')
    A1[0,:]=0

    for m in range(1, N+1):
        sets2=create_setl(m, N, 1)
        i=0
        for setx in sets2:
            print setx, 'setx'
            if m<2:
                j=setx[1]
                A1[j-1, i]=dist[1,j]
                i+=1
    
                print A1, 'A1', m, 'm'
            else:
                A2=np.zeros([N, len(sets2)])+float('+inf')
                A2[0,:]=0
                for j in setx:
                    a=[]
                    print j, 'j'
                    if j!=1:
                        i2=sets2.index(setx)
                        y=copy.deepcopy(setx)
                        y.remove(j)
                        i1=sets1.index(y)
                        print i2, 'i2', i1, 'i1', y, 'y', sets1, 'sets1'
                        for k in y:
                            d=dist[(min(k,j), max(k,j))]
                            x=A1[j-1, i1]+d
                            a.append(x)
                        A2[j-1,i2]=min(a)
                        
                
             
                del sets1
                sets1=copy.deepcopy(sets2)
                del A1
                A1=copy.deepcopy(A2)
                print sets2, 'sets2'
                print A1, 'A1', m
    print sets1
    return A2
                    