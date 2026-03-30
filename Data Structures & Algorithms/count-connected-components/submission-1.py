class UnionFind:
    def __init__(self, n):
        self.par, self.rank = [i for i in range(n)], [1] * n


    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x


    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False # union not possible

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]

        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges or not edges[0]:
            return 0
        uf = UnionFind(n) # n = num verticies in the graph
        rootToComponent = defaultdict(list)

        for a, b in edges:
            uf.union(a, b)

        for i in range(n):
            leader = uf.find(i)
            rootToComponent[leader].append(i)
        print(rootToComponent)
        return len(rootToComponent)