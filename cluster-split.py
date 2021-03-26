from random import randint,shuffle
from collections import defaultdict
from math import inf
from functools import reduce
import networkx as nx
from VA import VA, cost_plus,cost_minus
from RN import RN

"""
Assumptions: 
- i was not incremented, used for loop with constant increment value of 1
- j was never initialized, initialized outside the loop by variable i 
"""

def ClusterSplit(G,cluster):
    best = -inf
    C = {}
    for c in cluster:
        cost = 0
        for i in c:
            cost += cost_plus(G,i,set(G.nodes)-c)
        if best < cost:
            C = c
            best = cost
    # print(best,C)
    cluster1 = []
    for c in cluster:
        if c != C:
            cluster1.append(c)
    cluster = cluster1
    # print(cluster1)
    best = -inf
    for c in C:
        cost = cost_plus(G,c,C)
        if cost > best:
            best = cost
            u = c
    C = C - {u}
    best = -inf
    for c in C:
        cost = cost_plus(G,c,C)
        if cost > best:
            best = cost
            v = c
    C -= {v}
    cu = {u}
    cv = {v}
    # print("cu:",cu,"cv:",cv)
    for w in C:
        # print(len(set(G.adj[w]).intersection(G.adj[u])))
        # print(len(set(G.adj[w]).intersection(G.adj[v])))
        if len(set(G.adj[w]).intersection(G.adj[u])) >= len(set(G.adj[w]).intersection(G.adj[u])):
            cu.add(w)
        else : 
            cv.add(w)
    cluster.append(cu)
    cluster.append(cv)
    # print(cluster)
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
print(ClusterSplit(G,c))
