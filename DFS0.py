import pickle

def vertex_names(graph, Dt): # change nodes names to new ones from Dt
	Dnew={}
	for k, v in Dt.items():
		l=[]
		for i in graph[k]:
			l.append(Dt[i])
		Dnew[v]=l
	return Dnew	
	
def DFS(graph, Dl, node):	# Dl is the same dict as graph, but values are logical if examined
	global t
	Dl[node]=True
	for i in graph[node]:
		if Dl[i]==False:
			Dl[i]=True
			DFS(graph, Dl, i)
	t+=1
	Dt[node]=t
	return Dt

def DFS_loop(graph):
	Dl={}
	Dt={}
	for i in graph:
		Dl[i]=False
	Dl2={k: v for k, v in Dl.items() if v==False}
	if len(Dl2)>0: node=max(Dl2)
	while len(Dl2)>0:
		Dt=DFS(graph, Dl, node)
		Dl2={k: v for k, v in Dl.items() if v==False}
		if len(Dl2)>0: node=max(Dl2)
	return Dt

def DFS2(graph, Dl, node):	# Dl is the same dict as graph, but values are logical if examined
	global S
	#S=0
	Dl[node]=True
	for i in graph[node]:
		if Dl[i]==False:
			Dl[i]=True
			DFS2(graph, Dl, i)
		#if i == graph[node][len(graph[node])-1]: 
			#Dl[i]=True
	S+=1
	return S

def DFS_loop2(graph):
	Dl={}
	global S
	Dscc={}
	for i in graph: 
		Dl[i]=False
	Dl2={k: v for k, v in Dl.items() if v==False}
	if len(Dl2)>0: node=max(Dl2)
	while len(Dl2)>0:
		#print 'node', node
		S=0
		Dscc[node]=DFS2(graph, Dl, node)
		Dl2={k: v for k, v in Dl.items() if v==False}
		if len(Dl2)>0: node=max(Dl2)
	return Dscc
	
	
	
D=pickle.load(open("D.p", 'rb'))
Dr=pickle.load(open('Dr.p', 'rb'))    # reversed D graph
t=0 # finishing time
S=0
Dt={}
Dt=DFS_loop(Dr)
#print Dt
Dnew=vertex_names(D, Dt)
Dscc=DFS_loop2(Dnew)
v=Dscc.values()
v.sort()
print v[:5]