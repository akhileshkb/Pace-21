def get_edges(C):
	edges = []
	for cluster in C:
		cluster = list(cluster)
		for i, u in enumerate(cluster):
			for j, v in enumerate(cluster):
				if i >= j:
					continue
				edges.append((u, v))

	return edges


def compute_cost(G, C):
	cur = set(G.edges)
	final = set(get_edges(C))

	edges_to_delete = final - cur
	edges_to_add = cur - final

	return len(edges_to_add) + len(edges_to_delete)