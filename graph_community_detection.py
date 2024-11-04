
import networkx as nx

class GraphCommunityDetector:
    def __init__(self):
        self.graph = nx.Graph()

    def analyze(self, transaction):
        self.graph.add_edge(transaction["account_from"], transaction["account_to"], weight=transaction["amount"])
        communities = nx.algorithms.community.greedy_modularity_communities(self.graph)
        for community in communities:
            if len(community) > 5:
                return True
        return False
    