S =0
def incursion(arr):
    global S
    if len(arr)==0: return
    if len(arr) > 1: 
        ar1=arr[:len(arr)/2]
        ar2=arr[len(arr)/2:]
        incursion(ar1)
        incursion(ar2)
        i,j, k=0,0,0
        while i<len(ar1) and j<len(ar2):
            if ar1[i]<ar2[j]:
                arr[k]=ar1[i]
                i+=1
            else:
                arr[k]=ar2[j]
                j+=1
                S+=len(ar1)-i
            k+=1    
        while i<len(ar1):
            arr[k]=ar1[i]
            i+=1
            k+=1
        while j<len(ar2):
            arr[k]=ar2[j]
            j+=1
            k+=1
    return S
    
import string 
 
data=open('integerarray.txt', 'r')
L=[]
for line in data:
    Nu=int(line.splitlines()[0])
    L.append(Nu)
data.close()
#print L
t=incursion(L)
t2=incursion([1,3,5,2,4,6])
print t, t2