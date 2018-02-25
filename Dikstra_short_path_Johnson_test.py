import pickle
import os
from Heap_min import *
from Bellman_Ford import *
import copy
items = [map(int, x.split(' ')) for x in open('PA4test3.txt', 'r').read().split('\n')[0:-1]]
print items
#gr=pickle.load(open('graph.pickle','r'))
#gr=pickle.load(open('Dikstra.p','rb'))

from Heap_min import *
def Dikstra_dict(graph):
    D={} # graph to dictionary, with values in heap
    for i in graph[1:len(graph)+1]:
        if i[0] not in D:
            D[i[0]]=Heap_min((i[1], i[3], i[0], i[2]))
        else:
            D[i[0]].insert((i[1],i[3], i[0], i[2]))
    return D

def create_vertex_s(items):
    for i in range(1, items[0][0]+1):
        items.append([items[0][0]+1, i, 0])
    items[0][0]=items[0][0]+1
    items[0][1]=items[0][1]+items[0][0]-1
    items2=copy.deepcopy(items)
    return items2


	
def reweight(items, A):
    newG=[]
    A=list(A)
    for i in items:
        if len(i)<3: newG.append(i)
        else:
            newl=int(i[2]+A[i[0]-1]-A[i[1]-1])
            newG.append([i[0], i[1], i[2], newl])
    return newG

def Dikstra_short_path(graph_dict, u): #, itemsCrew):
    #Dg=graph_extend(itemsCrew)
    visited=[]    # u is starting vertex
    edges=[]      #explored edges
    #print Dg #graph_dict, graph_dict[1].ar#vertexes=graph_dict.keys()
    vertexes=range(1,1001)
    tovisit=set(vertexes)
    #path=[]#print tovisit, 'tv'
    dist=[float('+inf')]*(len(vertexes)+1)
    if u not in graph_dict:
        dist[u]=0
        output=[[u], dist]
        return output
        #break
    
    outgoing=copy.deepcopy(graph_dict[u])
    #print graph_dict[1].ar, '0test'    #output=[[u], dist[u]=0]
    dist[u]=0 #outgoing.ar[0][1]#dist[u]=0 #pl=0  # path length
    visited.append(u)
    tovisit.remove(u)
    vertex=(outgoing.ar[0][0], outgoing.ar[0][1], outgoing.ar[0][2])
    output=[visited, dist]
    while len(outgoing.ar)>0:
        #vertex=outgoing.ar
        #print 'v', vertex 
        #vertex=(outgoing.ar[0][0], outgoing.ar[0][1], e1)
        outgoing.extract_root()
        #pl=vertex[1]#print graph_dict[1].ar, 'test'
        u=vertex[0]
        #e2=u 		# goto next
        #print 'vertex', vertex, outgoing.ar, tovisit
        pl=vertex[1]
        if u in tovisit:
            tovisit.remove(u)
        out=[]  
        edges.append((vertex[2],vertex[0]))#print graph_dict[1].ar,  'ooooo'		
        op=[]
        #print outgoing.ar, 'ar'
        if len(outgoing.ar)>1:
            for oo in outgoing.ar:#if len(path)>0: 
                op.append((oo[0], oo[1], oo[2]))#pp=path[-1]+D[(e1,e2)][0]
            outgoing=Heap_min(op)        
        elif len(outgoing.ar)==1: 
            op=(outgoing.ar[0][0], outgoing.ar[0][1], outgoing.ar[0][2])
            outgoing=Heap_min(op) 
        #print op
        #outgoing=Heap_min(op)#    print e1, e2, Dg		
        #    path.append(path[-1]+Dg[(e1,e2)][0])
        #else: path.append(Dg[(e1,e2)][0])		
        if u in graph_dict:
            if len(graph_dict[u].ar)==1:
                
                #print graph_dict[u].ar, u, 'kkkkkk'
                out.append((graph_dict[u].ar[0][0], graph_dict[u].ar[0][1]+pl, graph_dict[u].ar[0][2]))			
            else:			
                
                #print graph_dict[u].ar, u, 'zzzzzzz'		
                for out_path in graph_dict[u].ar:
                    out.append((out_path[0], out_path[1]+pl, out_path[2]))
            #print 'out', out				
            li=outgoing.ar+out
        else: li=outgoing.ar
        #print 'updated', li, tovisit
        linew=[]
        visited.append(u)		
        if len(li)>1:
            for i in li:
                if i[0] not in visited:
                    linew.append(i)
        elif len(li)==1:
            if li[0][0] not in visited:
                linew.append(li[0])
        #print linew, 'li'			
        if len(linew)<1: 
            #visited.append(u)
            dist[u]=pl
            #edges.append((e1,e2))			
            output=[dist, edges]
            return output
            break
        outgoing=Heap_min(linew)
        #print vertex, pl, outgoing.ar, 'u & visited', u, visited, 'edges', edges
        vertex=outgoing.ar[0]
        dist[u]=pl
        #print vertex, pl, outgoing.ar, 'u & visited', u, visited, 'edges', edges
        #os.system('pause')
    output=[dist, edges]
    return output
	

def many_sources(Graph, itemsCrew):
	#print itemsCrew
	n=itemsCrew[0][0]
	#print 'n', n
	Dg=graph_extend(itemsCrew)
	#nn=itemsCrew[0][0]
	#dist=[float('+inf')]*(nn+1)
	DDD=[]
	#dist=[float('+inf')]*(len(vertexes)+1)
	for k in Graph:
		dis=list([float('+inf')]*(n+1))
		dis[k]=0
		#print dis
		a=Dikstra_short_path(Graph, k) #, itemsCrew)
		
		print k
		
		for m in a[1]:
			#print m, k, dis
			dis[m[1]]=Dg[m][0]+dis[m[0]]
		#print k, dis
		DDD.append(min(dis))
		
	return DDD
		
		
def graph_extend(graph):
	Dg={}
	graph.pop(0)
	for i in graph:
		#print i
		k=(i[0], i[1])
		#if k in D.keys():
		Dg[k]=(i[2], i[3])
		
	return Dg
	
# this section to calculate weights	
items2=create_vertex_s(items)
items = [map(int, x.split(' ')) for x in open('PA4test3.txt', 'r').read().split('\n')[0:-1]]

print 'items2', items2, 
print 'items', items
#print items2[len(items2)-1][0]
A=Bellman_Ford(items2,items2[len(items2)-1][0])
Alast=A[len(A)-1]
#print Alast, "Alast"
# or load them:	
#A=pickle.load(open("PA4c.pickle", 'rb'))
#Alast=A[len(A)-1]


itemsCrew=reweight(items, Alast)
##print 'hre', items, itemsCrew
Graph=Dikstra_dict(itemsCrew) # move graph to dictionary, with heaps in values()
print items
print Graph[1].ar
#print itemsCrew
dist=many_sources(Graph, itemsCrew)
print min(dist) #Graph[1].ar
#os.system('pause')
#a=Dikstra_short_path(Graph, 3)
#print a

