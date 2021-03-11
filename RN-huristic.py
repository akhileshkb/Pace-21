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


def RN(G, k_min=0, k_max=2):
	"""RN Huristics implementation

	Args:
		G (Networkx): Graph in Networkx format
		k_min (Int): Hyperparameter
		k_max (Int): Hyperparameter
	"""
	k, j = randint(k_min, k_max), 0
	v, n = list(G.nodes), len(G.nodes)
	v.sort(key=lambda x: len(G.adj[x]), reverse=True)
	c = [{x} for x in v]
	RelativeCost = defaultdict(lambda: inf)

	# while k + 1 <= i <= n:
	for i in range(k+1, n+1):
		while 1 <= j <= k:
			RelativeCost[(v[i], frozenset(c[j]))] = cost_plus(G, v[i], c[j]) - cost_minus(G, v[i], c[j])
			if RelativeCost[(v[j], c[j])] < RelativeCost[(v[i], c[1])]:
				c[j] = c[j] | {v[i]}
				RelativeCost[(v[j], c[i])] = RelativeCost[(v[i], c[j])]
			else:
				j += 1

	return reduce(lambda x, y: x | y, c)


G = {
	0: {1},
	1: {0, 3, 4},
	2: {5},
	3: {1, 4},
	4: {1, 3},
	5: {2}
}
G = nx.Graph(G)


print(RN(G))
