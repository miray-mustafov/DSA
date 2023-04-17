from collections import deque


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, start, end):
        queue = deque([start])
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == end:
                return True
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return False

customDict = {"a": ["c", "d", "b"],
              "b": ["j"],
              "c": ["g"],
              "d": [],
              "e": ["f", "a"],
              "f": ["i"],
              "g": ["d", "h"],
              "h": [],
              "i": [],
              "j": []
              }

g = Graph(customDict)
print(g.checkRoute("a", "j"))
print(g.checkRoute("a", "z"))
