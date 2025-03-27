class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, " : ", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False 
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        # check if both vertices are exist or not
        if v1 in self.adj_list and v2 in self.adj_list:
            # if there is no edge between both the vertices 
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True 
        return False
    

    
my_graph = Graph() 
my_graph.add_vertex('A') 
my_graph.add_vertex('B') 
my_graph.add_vertex('C') 
my_graph.add_vertex('D') 

my_graph.add_edge('A', 'B')
my_graph.add_edge('D', 'B')
my_graph.add_edge('A', 'D')
my_graph.add_edge('D', 'C')
my_graph.add_edge('A', 'C')

# my_graph.remove_edge('A', 'B')
# my_graph.remove_edge('A', 'D')

my_graph.remove_vertex('D')

my_graph.print_graph() 

