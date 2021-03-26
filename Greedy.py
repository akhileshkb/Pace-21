from random import randint
from collections import defaultdict
from math import inf
from functools import reduce
import networkx as nx

"""
Assumptions: 
- i was not incremented, used for loop with constant increment value of 1
- j was never initialized, initialized outside the loop by variable i 
"""


def cost_plus(G, node, nodes):
	"""cost of adding 'node' to the set 'nodes'

	Args:
		G (Networkx): Input graph
		node (Int): node to be added
		nodes (List[Int]): List of nodes from the graph G

	Returns:
		Int: required cost
	"""
	nodes = set(nodes)
	cur = set(G.adj[node])

	return len(nodes - cur)


def cost_minus(G, node, nodes):
	"""Cost of deleting 'node' from set 'nodes'

	Args:
		G (Networkx): Input Graph
		node (Int): node to be removed
		nodes (List[Int]): List of nodes from graph G

	Returns:
		Int: required cost
	"""
	nodes = set(nodes)
	cur = set(G.adj[node])

	return len(cur - nodes)

def sorting_cost(u, v, G):
	u_neigh, v_neigh = set(G.adj[u]), set(G.adj[v])
	if (u, v) in G.edges:
		return u_neigh.intersection(v_neigh).__len__()*2 + 1
	else:
		all_nodes = u_neigh.union(v_neigh).union({u, v})
		_cnt = 0
		for x in all_nodes:
			for y in all_nodes:
				if x == y:
					continue
				elif (x, y) not in G.edges:
					_cnt += 1
		return _cnt


def Greedy(G, k=0):
	"""RN Huristics implementation

	Args:
		G (Networkx): Graph in Networkx format
		k_min (Int): Hyperparameter
		k_max (Int): Hyperparameter
	"""

	nodes = list(G.nodes)
	pair_nodes = [(x, y) for x in nodes for y in nodes if x != y]
	pairs_nodes = {tuple(item) for item in map(sorted, pair_nodes)}
	pairs_of_nodes = [(x, y, sorting_cost(x, y, G)) for x, y in pairs_nodes]
	
	pairs_of_nodes.sort(key = lambda x: x[-1])

	# for index, edge in enumerate(pairs_of_nodes):
		# if k < edge[-1]:
			# return pairs_of_nodes[:index]
		# k -= edge[-1]

	return pairs_of_nodes


def get_edges(edges, G):
	modified_edges = []
	marked = []
	# run(karde)
	for edge in edges:
		u, v, _cost = edge
		if u in marked:
			continue
		if v in marked:
			continue

		# if (u, v) exists as edge
		if v in G.adj[u]:
			# delete it and common neighbourhood edges
			neighbour_nodes = set(G.adj[u]).intersection(set(G.adj[v]))
			for node in neighbour_nodes:
				modified_edges.extend([(node, u), (node, v)])
				marked.append(node)
			modified_edges.append((u, v))
			marked.extend([u, v])

		else:
			# add it and get all neighbours
			neighbour_nodes = set(G.adj[u]).union(set(G.adj[v])).union({u, v})
			for node_u in neighbour_nodes:
				for node_v in neighbour_nodes:
					if node_u == node_v:
						continue
					elif node_u in G.adj[node_v]:
						continue
					elif node_v in G.adj[node_u]:
						continue
					modified_edges.append((node_u, node_v))
					marked.extend([node_u, node_v])
	
	modified_edges = list({tuple(item) for item in map(sorted, modified_edges)})
	return modified_edges



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


print(get_edges(Greedy(G, 1), G))
