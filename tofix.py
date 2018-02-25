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
    e1=u
    vertex=(outgoing.ar[0][0], outgoing.ar[0][1], e1)
    output=[visited, dist]
    while len(outgoing.ar)>0:
        #vertex=outgoing.ar
        #print 'v', vertex 
        #vertex=(outgoing.ar[0][0], outgoing.ar[0][1], e1)
        outgoing.extract_root()
        #pl=vertex[1]#print graph_dict[1].ar, 'test'
        u=vertex[0]
        e2=u 		# goto next
        #print 'vertex', vertex, outgoing.ar, tovisit
        pl=vertex[1]
        if u in tovisit:
            tovisit.remove(u)
        out=[]  
        edges.append((vertex[2],e2))#print graph_dict[1].ar,  'ooooo'		
        op=[]
        #print outgoing.ar, 'ar'
        if len(outgoing.ar)>1:
            for oo in outgoing.ar:#if len(path)>0: 
                op.append((oo[0], oo[1], e1))#pp=path[-1]+D[(e1,e2)][0]
            outgoing=Heap_min(op)        
        elif len(outgoing.ar)==1: 
            op=(outgoing.ar[0][0], outgoing.ar[0][1], e1)
            outgoing=Heap_min(op) 
        #print op
        #outgoing=Heap_min(op)#    print e1, e2, Dg		
        #    path.append(path[-1]+Dg[(e1,e2)][0])
        #else: path.append(Dg[(e1,e2)][0])		
        if u in graph_dict:
            if len(graph_dict[u].ar)==1:
                e1=copy.deepcopy(e2)
                #print graph_dict[u].ar, u, 'kkkkkk'
                out.append((graph_dict[u].ar[0][0], graph_dict[u].ar[0][1]+pl, e1))			
            else:			
                e1=copy.deepcopy(e2)
                #print graph_dict[u].ar, u, 'zzzzzzz'		
                for out_path in graph_dict[u].ar:
                    out.append((out_path[0], out_path[1]+pl, e1))
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
		#edges.append((e1,e2))#visited.append(u)
        #e1=copy.deepcopy(e2)#tovisit.remove(u)		#
        dist[u]=pl
        #print vertex, pl, outgoing.ar, 'u & visited', u, visited, 'edges', edges
        #os.system('pause')
    output=[dist, edges]
    return output
	.