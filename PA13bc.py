edges = [map(int, x.split(' ')) for x in open('PA13.txt', 'r').read().split('\n')[1:-1]]
vertices = set()
import os
print edges[0]
for edge in edges:
    vertices.add(edge[0])
    vertices.add(edge[1])
spanned = set()
spanned.add(vertices.pop())

total_cost = 0
while len(vertices)>0:
    best_cost = 9999999
    for edge in edges:
        if edge[0] in spanned and edge[1] in vertices and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[1]
        if edge[1] in spanned and edge[0] in vertices and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[0]
    spanned.add(best_vert)
    vertices.remove(best_vert)
    total_cost+=best_cost

    print vertices
    print best_cost, 'cost'
    print best_vert, 'go to'
    print spanned, 'spanned'
    os.system('pause')
#    print total_cost
print total_cost