class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_node(self, value):
        self.nodes.append(value)

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def print_solution(self, dist):
        print("\nVertex Distance and Predecessor from Source")
        for key, value in dist.items():
            print('  ' + key, ':', value)

    def print_paths(self, vertices, src):
        print(f"\nVertices paths from {src}")
        for key, value in vertices.items():
            if key == src:
                continue
            path = key
            pred = value['predecessor']
            while pred is not None:
                path += '<' + pred
                pred = vertices[pred]['predecessor']

            print('  ' + key, ':', path)

    def bellmanFord(self, src):
        vertices = {i: {'distance': float("Inf"), 'predecessor': None} for i in self.nodes}
        a = 5
        vertices[src]['distance'] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if vertices[s]['distance'] != float("Inf") and vertices[s]['distance'] + w < vertices[d]['distance']:
                    vertices[d]['distance'] = vertices[s]['distance'] + w
                    vertices[d]['predecessor'] = s

        for s, d, w in self.graph:
            if vertices[s]['distance'] != float("Inf") and vertices[s]['distance'] + w < vertices[d]['distance']:
                print("Graph contains negative cycle")
                return

        self.print_solution(vertices)
        self.print_paths(vertices, src)


g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")
