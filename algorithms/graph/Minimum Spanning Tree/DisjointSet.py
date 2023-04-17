
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


vertices = ["A", "B", "C", "D", "E", 'F', 'G']

ds = DisjointSet(vertices)
ds.union("A", "B")
ds.union("A", "C")
ds.union("A", "G")
ds.union("D", "E")
ds.union("E", "F")
ds.union("A", "F")

print(ds.find("E"))