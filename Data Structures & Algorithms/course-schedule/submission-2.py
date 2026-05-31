class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = collections.defaultdict(list)
        n = numCourses
        for src, dst in prerequisites:
            mapping[src].append(dst)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        crs = [UNVISITED] * n


        def dfs(node):
            if crs[node] == VISITING: return False
            if crs[node] == VISITED: return True

            crs[node] = VISITING
            for nei in mapping[node]:
                if not dfs(nei): return False

            crs[node] = VISITED
            return True


        for i in range(n):
            if not dfs(i): return False
        return True