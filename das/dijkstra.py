class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = list(graph.keys())
        self.distances = {}
        self.predecessors = {}
        self.visited = []

    def find_shortest_path(self, start_node, end_node):
        self.distances[start_node] = 0
        self.predecessors[start_node] = None
        self.visited.append(start_node)
        self._visit(start_node, end_node)
        return self._get_path(start_node, end_node)

    def _visit(self, node, end_node):
        if node == end_node:
            return
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.visited.append(neighbor)
                self._update_distance(node, neighbor)
        next_node = self._find_next_node()
        self._visit(next_node, end_node)

    def _update_distance(self, node, neighbor):
        new_distance = self.distances[node] + self.graph[node][neighbor]
        if neighbor not in self.distances or new_distance < self.distances[neighbor]:
            self.distances[neighbor] = new_distance
            self.predecessors[neighbor] = node

    def _find_next_node(self):
        unvisited = {}
        for node in self.nodes:
            if node not in self.visited:
                unvisited[node] = self.distances[node]
        return min(unvisited, key=unvisited.get)

    def _get_path(self, start_node, end_node):
        path = [end_node]
        node = end_node
        while node != start_node:
            node = self.predecessors[node]
            path.append(node)
        return path[::-1]
