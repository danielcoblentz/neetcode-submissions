class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * n

        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)

        def solve(node):
            state = states[node]
            if state == VISITING: return False
            if state == VISITED: return True

            states[node] = VISITING

            for nei in adj[node]:
                if not solve(nei):
                    return False

            states[node] = VISITED
            res.append(node)
            return True

        for i in range(n):
            if states[i] == UNVISITED:
                if not solve(i): return []

        return res[::-1]
