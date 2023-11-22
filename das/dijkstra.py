import unittest



# return all shortest paths between start and end
def dijkstra(graph, start, end):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    
    # return path if start is goal
    if start == end:
        return "That was easy! Start = end"
    
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                # return path if neighbour is goal
                if neighbour == end:
                    return new_path
            
            # mark node as explored
            explored.append(node)
            
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

# Test the algorithm
class Test(unittest.TestCase):
    def test_dijkstra(self):
        graph = {
            'A': [('B', 10), ('C', 3)],
            'B': [('C', 1), ('D', 2)],
            'C': [('B', 4), ('D', 8), ('E', 2)],
            'D': [('E', 7)],
            'E': [('D', 9)]
        }
      
        
        
        
        self.assertEqual(dijkstra(graph, 'A', 'E'), ['A', 'C', 'E'])
        self.assertEqual(dijkstra(graph, 'A', 'D'), ['A', 'C', 'E', 'D'])
        self.assertEqual(dijkstra(graph, 'E', 'A'), "So sorry, but a connecting path doesn't exist :(")
        self.assertEqual(dijkstra(graph, 'A', 'A'), 'That was easy! Start = end')
        

if __name__ == "__main__":
    unittest.main()
    
    
    