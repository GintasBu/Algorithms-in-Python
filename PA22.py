edges = [map(int, x.split(' ')) for x in open('PA22.txt', 'r').read().split('\n')[1:-1]]
vertices = set()
#print edges
for edge in edges:
    vertices.add(edge[0])
    vertices.add(edge[1])
spanned = set()
spanned.add(vertices.pop())

total_cost = 0
print edges[0]