from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self,directed):
        self.graph = defaultdict(list)
        self.directed = directed 

    def add_edge(self, u,v,weight):
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self,current_node, goal_node):
        visited = []
        queue = PriorityQueue()
        queue.put((0, current_node))

        while not queue.empty():
            item = queue.get()
            current_node = item[1]

            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue

                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                    queue.put((neighbour[0], neighbour[1]))

g = Graph(False)

# g.graph =  defaultdict(list)
# g.add_edge('S', 'A', 1)
# g.add_edge('S', 'G', 12)
# g.add_edge('A', 'B', 3)
# g.add_edge('A', 'C', 1)
# g.add_edge('C', 'D', 1)
# g.add_edge('B', 'D', 3)
# g.add_edge('C', 'G', 2)
# g.add_edge('D', 'G', 3)

g.graph =  defaultdict(list)
g.add_edge('A', 'C', 3)
g.add_edge('A', 'B', 7)
g.add_edge('C', 'D', 9)
g.add_edge('C', 'B', 2)
g.add_edge('B', 'E', 6)
g.add_edge('D', 'H', 13)
g.add_edge('D', 'E', 3)
g.add_edge('E', 'F', 2)
g.add_edge('E', 'G', 1)

g.graph

g.ucs('A','H')