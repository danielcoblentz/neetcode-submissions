class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1: return True
        unvisited, visiting, visited = 0, 1, 2
        states = [unvisited] * numCourses
        adj = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)

        def solve(node, states):
            state = states[node]

            if state == 1: return False
            elif state == 2: return True

            states[node] = 1

            for nei in adj[node]:
                if not solve(nei, states): return False
            states[node] = 2
            return True

        for i in range(numCourses):
            if not solve(i, states): return False
        return True