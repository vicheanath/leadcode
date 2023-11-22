
class BFS:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.queue = [start]
        self.visited = [start]
        self.parent = {start: None}
        self.level = {start: 0}
        self.bfs()

    def bfs(self):
        while self.queue:
            current = self.queue.pop(0)
            for neighbor in self.graph[current]:
                if neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.append(neighbor)
                    self.parent[neighbor] = current
                    self.level[neighbor] = self.level[current] + 1

    def get_path(self, goal):
        path = []
        while goal != self.start:
            path.append(goal)
            goal = self.parent[goal]
        path.append(self.start)
        path.reverse()
        return path

    def get_level(self, node):
        return self.level[node]