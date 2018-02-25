#load data
import pickle
import copy
D=pickle.load(open("D.p", 'rb'))
#Dr=picle.load(open('Dr.p', 'rb'))
t=0 # finishing time
Dl={}
Dt={}
for i in D:
	Dl[i]=False
Dl2=copy.deepcopy(Dl)
def DFS(graph, Dl, node):	# Dl is the same dict as graph, but values are logical if examined
	global t
	#global Dt
	Dl2={k: v for k, v in Dl.items() if v==False}
	node0=max(Dl2)
	print node0
	while node0>0:
		Dl2={k: v for k, v in Dl.items() if v==False}
		#print len(Dl2)
		if Dl[node]==False: 
			#node=max(Dl2)
			print 'node', node
			
			
			Dl[node]=True
			for i in graph[node]:
				print 'i', i
				if Dl[i]==False:
					Dl[i]=True
					DFS(graph, Dl, i)
					t+=1
					Dt[i]=t
	#t+=1
			Dt[node]=t+1
	#print t
		#Dl2={k: v for k, v in Dl.items() if v==False}
		node0=max(Dl2)
		#print 'node0', node0, Dl2
	return Dt