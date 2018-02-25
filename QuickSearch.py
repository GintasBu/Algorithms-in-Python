S =0
def quicksearch(arr):
    global S
    N=len(arr)
    if N<=1: return arr
    else:
        pivot=arr[0]
        i=1
        for j in range(1, N):
            if arr[j]<pivot:
                arr[i], arr[j]=arr[j], arr[i]
                i+=1
        S+=j
        #print S, j
        arr[0], arr[i-1]=arr[i-1], arr[0]
        #arr[N-1], arr[i-1]=arr[i-1], arr[N-1]
        ar1=quicksearch(arr[:i-1])
        ar2=quicksearch(arr[i:])
        return S #ar1+[arr[i-1]]+ar2
    
import string 
 
data=open('integerarrayB.txt', 'r')
L=[]
for line in data:
    Nu=int(line.splitlines()[0])
    L.append(Nu)
data.close()
#print L
t=quicksearch(L)
print t