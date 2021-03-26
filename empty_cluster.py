from random import randint,shuffle
from collections import defaultdict
from math import inf
from functools import reduce
import networkx as nx
from VA import VA, cost_plus,cost_minus
from RN import RN

def EmptyCluster(G,cluster):
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
	print(C)
	C = list(C)
	index = 0
	while index < len(C):
		w = C[index]
		# print(w)
		# c = cost_plus(G,w,set(C))
		best = cost_plus(G,w,set(C))
		C.pop(index)
		flag = 0
		for clus in cluster:
			print(best, cost_plus(G,w,clus))
			if best < cost_plus(G,w,clus):
				print("in")
				best = cost_plus(G,w,clus)
				c1 = clus
				flag = 1
		if flag: c1.add(w)
		else : 
			C.insert(index,w)
			index+=1
	C = set(C)
	cluster.append(C)
	return cluster

G = {
	0: {1, 2, 3},
	1: {0, 2},
	2: {0, 1, 3},
	3: {0, 2},
	4: {5, 6},
	5: {4, 6},
	6: {4, 5}
}
G = nx.Graph(G)

c,_ = VA(G)
print(c)
print(EmptyCluster(G,c))
