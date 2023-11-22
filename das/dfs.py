
    
class DFS:
    """
    Depth-first search algorithm.
    """
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.parent = {}
        self.entry = {}
        self.exit = {}
        self.time = 0

    def run(self, start=None):
        """
        Run DFS on the graph.
        """
        if start is None:
            for v in self.graph.vertices:
                if v not in self.visited:
                    self._dfs(v)
        else:
            self._dfs(start)

    def _dfs(self, v):
        """
        Run DFS on the graph starting at v.
        """
        self.visited.add(v)
        self.entry[v] = self.time
        self.time += 1
        for u in self.graph.neighbors(v):
            if u not in self.visited:
                self.parent[u] = v
                self._dfs(u)
        self.exit[v] = self.time
        self.time += 1

    def path(self, start, end):
        """
        Return a path from start to end.
        """
        if start == end:
            return [start]
        elif end not in self.parent:
            return None
        else:
            path = self.path(start, self.parent[end])
            if path is None:
                return None
            else:
                return path + [end]

    def is_ancestor(self, u, v):
        """
        Return True if u is an ancestor of v.
        """
        return self.entry[u] <= self.entry[v] and self.exit[u] >= self.exit[v]

    def is_descendant(self, u, v):
        """
        Return True if u is a descendant of v.
        """
        return self.is_ancestor(v, u)

    def is_connected(self, u, v):
        """
        Return True if u and v are connected.
        """
        return self.is_ancestor(u, v) or self.is_ancestor(v, u)

    def is_tree_edge(self, u, v):
        """
        Return True if (u, v) is a tree edge.
        """
        return self.parent[v] == u

    def is_back_edge(self, u, v):
        """
        Return True if (u, v) is a back edge.
        """
        return self.is_descendant(u, v) and not self.is_tree_edge(u, v)

    def is_forward_edge(self, u, v):
        """
        Return True if (u, v) is a forward edge.
        """
        return self.is_descendant(v, u) and not self.is_tree_edge(u, v)
    
    def is_cross_edge(self, u, v):
        """
        Return True if (u, v) is a cross edge.
        """
        return not self.is_descendant(u, v) and not self.is_descendant(v, u)