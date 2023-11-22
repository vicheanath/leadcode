
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.node_count = 0
        self.edge_count = 0

    def add_node(self, node):
        self.nodes.append(node)
        self.node_count += 1

    def add_edge(self, edge):
        self.edges.append(edge)
        self.edge_count += 1

    def get_node(self, index):
        return self.nodes[index]

    def get_edge(self, index):
        return self.edges[index]

    def get_node_count(self):
        return self.node_count

    def get_edge_count(self):
        return self.edge_count

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_adjacency_matrix(self):
        matrix = []
        for i in range(self.node_count):
            matrix.append([])
            for j in range(self.node_count):
                matrix[i].append(0)

        for edge in self.edges:
            matrix[edge.get_source()][edge.get_target()] = edge.get_weight()

        return matrix

    def get_adjacency_list(self):
        adjacency_list = []
        for i in range(self.node_count):
            adjacency_list.append([])

        for edge in self.edges:
            adjacency_list[edge.get_source()].append(edge)

        return adjacency_list

    def get_adjacency_list_with_weights(self):
        adjacency_list = []
        for i in range(self.node_count):
            adjacency_list.append([])

        for edge in self.edges:
            adjacency_list[edge.get_source()].append((edge.get_target(), edge.get_weight()))

        return adjacency_list

    def get_adjacency_list_with_weights_and_nodes(self):
        adjacency_list = []
        for i in range(self.node_count):
            adjacency_list.append([])

        for edge in self.edges:
            adjacency_list[edge.get_source()].append((edge.get_target(), edge.get_weight(), self.nodes[edge.get_target()]))

        return adjacency_list

    def get_adjacency_list_with_nodes(self):
        adjacency_list = []
        for i in range(self.node_count):
            adjacency_list.append([])

        for edge in self.edges:
            adjacency_list[edge.get_source()].append((edge.get_target(), self.nodes[edge.get_target()]))

        return adjacency_list
            