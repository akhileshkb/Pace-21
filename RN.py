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


def RN(G, k_min=1, k_max=5):
	"""RN Huristics implementation

	Args:
		G (Networkx): Graph in Networkx format
		k_min (Int): Hyperparameter
		k_max (Int): Hyperparameter
	"""
	k, j = randint(k_min, k_max), 1
	v, n = list(G.nodes), len(G.nodes)
	v.sort(key=lambda x: len(G.adj[x]), reverse=True)
	c = [{x} for x in v[:k]]
	# print(c)
	RelativeCost = defaultdict(lambda: inf)

	# while k + 1 <= i <= n:
	for i in range(k, n):
		# print("idhar")
		index, best = 0, -inf
		while 0 <= j < k:
			RelativeCost[(v[i], frozenset(c[j]))] = cost_plus(G, v[i], c[j]) - cost_minus(G, v[i], c[j])
			# print(RelativeCost, i, j)
			if best < RelativeCost[(v[i], frozenset(c[j]))]:
				best = RelativeCost[(v[i], frozenset(c[j]))]
				index = j
				# print(i, j, "hello")
			j += 1
		c[index] = c[index] | {v[i]}

	print(c)
	return reduce(lambda x, y: x | y, c)


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


print(RN(G))