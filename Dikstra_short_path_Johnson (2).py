import pickle
import os
from heap_min import *
gr=pickle.load(open('Graph_dict.pickle','rb'))
#gr=pickle.load(open('Dikstra.p','rb'))
def Dikstra_short_path(graph_dict, u):
    visited=set()    # u is starting vertex
    vertexes=graph_dict.keys()
    tovisit=set(vertexes)
    dist=[float('+inf')]*(len(vertexes)+1)
    outgoing=graph_dict[u]
    pl=0  # path length
    visited.add(u)
    tovisit.remove(u)
    while len(outgoing.ar)>0:
        vertex=outgoing.ar[0]
        outgoing.extract_root()
        u=vertex[0] # goto next
        pl=vertex[1]
        dist[u]=pl
        visited.add(u)
        tovisit.remove(u)
        out=[] 
        for out_path in graph_dict[u].ar:
            out.append((out_path[0], out_path[1]+pl))			
        li=outgoing.ar+out
        linew=[]
        for i in li:
            if i[0] not in visited:
                linew.append(i)
        if len(linew)<1: break
        outgoing=Heap_min(linew)
    return dist
	
a=Dikstra_short_path(gr, 1)
li=[7,37, 59, 82, 99, 115, 133, 165, 188, 197]
for b in li:
	print b, a[b]