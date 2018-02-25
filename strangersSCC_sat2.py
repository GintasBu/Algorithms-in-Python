nx=875714  		# number of vertices in the original graph 69.3MB  text file.
nx=2000000			# testcase size.
graphmarks=[0]*nx; 	# a global matrix to keep track of vertices traversed
finishing_time=[];	# finishing_time is the order i.e. stack after complete traversing the graph by DFS 
stack=[];		# A list representing the function call stack. pyhton recursion stack not enough.  
sizes=[];		# the final list to store the size of SCC's
cluster=set()
clusters=[]

"""
Implement the Kosaraju's algorithm to compute the SCCs present in a graph.
Algorithm -- 
1) Traverse the graph with reversed edges using DFS in decreasing order of vertex number
2) Store the order in which edges were traversed like a stack in a list
3) Traverse the graph with proper edges using DFS starting from the last entry in the above list.
4) Every time the subroutine i.e DFS routines corresponds to a SCC. 
Finishing time
O(m+n) => m =  no.of edges and n= no. of vertices
"""

def initialize():	#initialize the graph to untraversed
    global graphmarks;
    graphmarks=[0]*nx;

def parse_graph(filename,reverse):
	global N
	graph=[];
	for i in range (0,nx):
		graph.append([]);
	inputfile=open(filename,"r");
	for line in inputfile.readlines():
		row=line.split();
		if len(row)<2: 
			N=int (row[0])
		else:
			#print N
			#print row
			if int(row[0])<0: 
				row[0]=int (row[0])#+N+1
			else: row[0]=int (row[0])#+N
			if int(row[1])<0:
				row[1]=int (row[1])#+N+1
			else: row[1]=int (row[1])#+N
			#print row
			if(reverse):
				if row[0]>0 and row[1]>0:
					graph[row[1]+N-1].append(1+N-row[0]);
					graph[row[0]+N-1].append(N-row[1]+1);
				if row[0]>0 and row[1]<0:
					graph[row[1]+N-1+1].append(1+N-row[0]);
					graph[row[0]+N-1].append(N-row[1]);#
				if row[0]<0 and row[1]>0:
					graph[row[0]+N-1+1].append(1+N-row[1]);
					graph[row[1]+N-1].append(N-row[0]);#
				if row[0]<0 and row[1]<0:
					graph[row[1]+N-1+1].append(N-row[0]);
					graph[row[0]+N-1+1].append(N-row[1]);
			else:
				if row[0]>0 and row[1]>0:
					graph[-row[1]+N].append(N+row[0]);
					graph[-row[0]+N].append(N+row[1]);
				if row[0]>0 and row[1]<0:
					graph[-row[0]+N].append(1+N+row[1]);
					graph[-row[1]+N-1].append(N+row[0]);#
				if row[0]<0 and row[1]>0:
					graph[-row[0]+N-1].append(N+row[1]);
					graph[-row[1]+N].append(N+1+row[0]);#
				if row[0]<0 and row[1]<0:
					graph[-row[1]+N-1].append(N+row[0]+1);
					graph[-row[0]+N-1].append(N+row[1]+1);
				#graph[row[0]-1].append(row[1]);
				
				#graph[row[0]-1].append(row[1]);
	inputfile.close();
	return graph;

def DFS_start(graph,flag):	#Start the DFS search,each run will result in a single SCC
	global graphmarks;
	global finishing_time;
	global stack
	#global cluster
	global clusters
	global sizes;
	initialize();
	if(flag):
		for x in range(len(graph),0,-1):
			if(graphmarks[x-1]==0):
				DFS(graph,x,flag);
	else:
		for x in finishing_time:
			if(graphmarks[x-1]==0):
				DFS(graph,x,flag);
  
def DFS(graph_dir,vertex,flag):	#Actual DFS traversal
  global graphmarks;
  global finishing_time;
  global stack
  #global cluster
  global clusters
  global sizes;
  cnt=0;
  cluster=set()
  graphmarks[vertex-1]=1;
  stack.append(vertex);
  number=vertex;
  while(True):
    for x in graph_dir[number-1]:
      if(len(graph_dir[number-1])==0):
	break;
      if(graphmarks[x-1]==0):
	graphmarks[x-1]=1;
	stack.append(x);	#push the vertex to stack and traverse the edges of x
	number=x;
	break;
    else:
      if(len(stack)==0):
	break;	  
      num=stack.pop();
      if(flag):
	finishing_time.append(num);	#store the order of traversal in stack
      else:
#	finishing_time.remove(num);
	cnt=cnt+1;
	cluster.add(num)
      if(len(stack)!=0):		# count the size of SCC and store in reverse traversal i.e second pass
         number=stack[len(stack)-1];
  if(not flag):
	sizes.append(cnt); 
	#cluster.add(num)
#  print "exited"	
	clusters.append(cluster)
  #print cluster
   	  
def satornot(clusters, N):
	while len(clusters)>0:
		cl=clusters.pop()
		while len(cl)>1:
			#print cl
			c1=cl.pop()
			if c1<=N:
				c2=N-c1+N+1
			else: c2=2*N-c1+1
			#print c1, c2, cl
			if c2 in cl: 
				print 'not satisfiable'
				return 
	print "satisfiable"
	return
	  
	  

if(__name__=="__main__"):
  graph1=parse_graph("PA66.txt",True);  	#parse the graph in reverse order   - row adjacency list
  print 'made reversed graph' #, graph1
  graph2=parse_graph("PA66.txt",False); 	#parse the grpah in straight order  - row adjacency list
  print 'made new grapgh'#, graph2
  DFS_start(graph1,True);  #first pass	
  print 'first pass completed'#, finishing_time
  finishing_time.reverse();			#reverse the finsihing times so as to start from last.
  DFS_start(graph2,False);			#second pass
  print 'second pass completed'
  sizes.sort(reverse=True);					
  print sizes[:10]
  print 'clusters'#, clusters, N
  rr=satornot(clusters, N)
  rr