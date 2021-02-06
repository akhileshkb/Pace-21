G = {
	0: {1},
	1: {0, 3, 4},
	2: {5},
	3: {1, 4},
	4: {1, 3},
	5: {2}
}

def dfs_connected_comps(graph, visited, node, nodes):
	if node in visited:
		return 
	visited.add(node)
	nodes.add(node)
	for neighbour in graph[node]:
		dfs_connected_comps(graph, visited, neighbour, nodes)


def get_connected_comp(graph):
	visited = set()
	comps = []
	for key in graph.keys():
		if key in visited:
			continue
		nodes = set()
		dfs_connected_comps(graph, visited, key, nodes)
		comps.append(nodes)
	return comps


def make_connected_comp_clique(graph, comps):
	for comp in comps:
		nodes = list(comp)
		# edge between each pair of nodes
		for u in nodes:
			for v in nodes:
				if u == v:
					continue
				graph[v].add(u)
				graph[u].add(v)


# print(get_connected_comp(G))

# cc = get_connected_comp(G)
# make_connected_comp_clique(G, cc)
# print(G)