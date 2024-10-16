from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self,directed):
        self.graph = defaultdict(list)
        self.directed = directed 

    def add_edge(self, u,v,x,y,weight):
        if self.directed:
            value = (weight, v,x,y)
            self.graph[u].append(value)
        else:
            value = (weight, v,x,y)
            self.graph[u].append(value)
            value = (weight, u,x,y)
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

g.graph =  defaultdict(list)

g.add_edge(0, 1, 0, 0, 0)
g.add_edge(0, 1, 0, 1, 0)
g.add_edge(0, 0, 0, 1, 0)
g.add_edge(0, 1, 0, 0, 0)
g.add_edge(0, 1, 0, 0, 0)


g.graph

g.ucs(0,1)



