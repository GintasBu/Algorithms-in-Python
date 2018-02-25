
import sys

class UnionFind(object):
    def __init__(self, n):
        self.tree = [0] * n
        self.tree_len = [1] * n
        for i in range(n):
            self.tree[i] = i

    def union(self, n1, n2):
        np1 = self.parent(n1)
        np2 = self.parent(n2)
    
        # This one is just to expedite the find, by reducing
        # the length of the tree. Makes it very fast.
        if (self.tree_len[np1] < self.tree_len[np2]):
            self.tree[np1] = np2
            self.tree_len[np2] += self.tree_len[np1]
        else:
            self.tree[np2] = np1
            self.tree_len[np1] += self.tree_len[np2]
    
    def parent(self, n1):
        dad = self.tree[n1]
        if(dad != n1):
            n1 = self.parent(dad)
        return n1

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()

    uf = UnionFind(int(lines[0]))
    edges = []
    for line in lines[1:]:
        line = map(lambda x: int(x), line.strip().split(" "))
        edges.append(line[-1:] + [line[0] - 1, line[1] - 1])
   
    # Sort in increasing order.
    edges = sorted(edges)

    n = int(lines[0])
    clusters = n
    # Implement Kruskal's MST to find Max-Space clustering for K=4.
    for i in range(len(edges)):
        cost, n1, n2 = edges[i]
        op1 = uf.parent(n1)
        op2 = uf.parent(n2)
        uf.union(n1, n2)
        np1 = uf.parent(n1)
        np2 = uf.parent(n2)
        # If nodes have switched their parent, means 
        # cluster count has dropped by 1.
        #
        # What is spacing?
        # It is the min distance between any two clusters.
        if op1 != np1 or op2 != np2:
            clusters -= 1
            if clusters == 4:
                ans = 999999
                i += 1
                while(i < len(edges)):
                    cost, n1, n2 = edges[i]
                    if uf.parent(n1) != uf.parent(n2):
                        if cost < ans:
                            ans = cost
                    i += 1
                print "Spacing: ", ans
                break
main()