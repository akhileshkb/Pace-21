from random import randint,shuffle
from collections import defaultdict
from math import inf
from functools import reduce
import networkx as nx
from VA import VA, cost_plus,cost_minus
from RN import RN

def VertexMove(G,cluster):
    for c in cluster:
        for i in c:
            c -= {i}
            for j in cluster:
                if j != c: 
                    # print(i,j)
                    if cost_plus(G,i,c) - cost_minus(G,i,c) < cost_plus(G,i,j) - cost_minus(G,i,j):
                        cluster.remove(c)
                        print(i,j)
                        c.remove(i)
                        print(c)
                        j.add(i)
                        break
        print(cluster)
    return cluster




G = {
	0: {1, 2, 3},
	1: {0, 2},
	2: {0, 1, 3},
	3: {0, 2},
	4: {0, 5, 6},
	5: {4, 6},
	6: {2, 4, 5}
}
G = nx.Graph(G)

c,_ = RN(G)
print(c)
print(VertexMove(G,c))
