class CriticalClique:
	def __init__(self, graph):
		self._graph = graph

	def _check_critical(self, u, v, critical_nodes):
		# u is already present in critical_nodes
		# check if v can be added to critical nodes
		# N(u) - critical_nodes = N(v) - critical_nodes, then v can be added
		n_u = set(self._graph.adj[u].keys())
		n_v = set(self._graph.adj[v].keys())

		if n_u - critical_nodes - {v} == n_v - critical_nodes - {u}:
			# critical_nodes.add(v)
			return True

		return False

	def _get_critical(self, node):
		critical = {node}

		for node in set(self._graph.adj.keys()) - critical:
			# for each remaining node in graph, check if it can
			# be added to the critical set
			if all(self._check_critical(node, other, critical) for other in critical):
				critical.add(node)

		return critical

	def num_critical(self):
		visited, count = set(), 0
		for node in self._graph.adj.keys():
			if node in visited:
				continue
			_set = self._get_critical(node)
			if len(_set):
				count += 1
			visited |= _set
		return count





import networkx as nx
# same example as explained in meet
G = nx.Graph([(1,2), (2,3), (3,4), (4,5), (5,6), (6,1), (6,2), (1,5),(5,2), (5,3), (2,4)])
G = CriticalClique(G)
print('Critical Clique having node 3: ', G._get_critical(3))
print(f'Num of critical cliques: {G.num_critical()}')
# print(G.adj)

'''
import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques
from networkx.classes.function import degree_histogram
from networkx.algorithms.components import number_connected_components
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

# WARNING: many networkx functions are not efficiently implemented (BAD TIME COMPLEXITY)

BASE_DIR = '/content/drive/MyDrive/PACE2021/heur'
file_name = '/heur001.gr'
file_path = BASE_DIR + file_name

file_path = '/home/harshraj22/Downloads/papers/SEM-6/data/heur/heur001.gr'


# pd.set_option('display.max_colwidth', None)
pd.set_option("max_columns", None) # show all cols
pd.set_option('max_colwidth', None) # show full width of showing cols
pd.set_option("expand_frame_repr", False) # print cols side by side as it's supposed to be

def get_graph(file_path):
	G = nx.Graph()
	with open(file_path, 'r') as f:
		num_nodes, num_edges = map(int, f.readline().split()[-2:])
		G.add_nodes_from(range(1, num_nodes+1))

		for line in f.readlines():
			if line.startswith(('c', 'p')):
				continue
			u, v = map(int, line.split())
			G.add_edge(u, v)

	return G

def get_statistics(file_path):
	G = get_graph(file_path)
	df = pd.DataFrame(columns=['Nodes', 'Edges', 'Most-Frequent-Degree', 'Connected-Components'])
	freq = degree_histogram(G)

	details = {
		'Nodes': len(G.nodes),
		'Edges': len(G.edges),
		'Most-Frequent-Degree': freq.index(max(freq)),
		'Connected-Components': number_connected_components(G)
	}
	df = df.append(details, ignore_index=True)
	# print(degree_histogram(G))

	# visualizing the Degree frequency
	# https://networkx.org/documentation/stable/reference/functions.html
	plt.bar(list(range(len(freq))), freq)

	plt.xlabel('Degree')
	plt.ylabel('Frequency')
	plt.grid(True)
	plt.title(file_name + ' => degree distribution')
	plt.show()

	# draw the graph using matplotlib
	# nx.draw(G)
	# plt.show()

	return df

print(get_statistics(file_path))
'''
"""
To do:
	comment the display part showing bar chart of matplotlib
	Iterate over all files and create dataframe containing statistics of all files
	save the dataframe as csv
"""