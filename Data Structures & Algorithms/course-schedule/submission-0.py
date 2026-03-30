'''

input: number of crs and list of prereq to take
output: booleans if true ca nfinis heverything ie no cycles found
if we find a cycle then we retunr false as it must be impossible

edge case:
no input, disconnected graph (outer for loop)

solution
build our adj list or grpah representation with dict --> asjlist
next populate it with the edge list

make dfs cycle detection function that operations in 3states

0 --> unvisited
1 --> visiting currenlty
2 --> complete no cycles down this part of graph

use states array to update this accordingly per node as we traverse the graph

if we get hte current state and it is currnelty visiting in our states array we return False cycle found other wise return true
if we dont hit any basecases we mark it as visited and retur ntrue

outter loop will go through every node in hte lsit (solves disconnected components problem)
and if not dfs: we found a cycle return false if we make it through everything we return true








'''



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        crs = prerequisites 

        # populate
        for dst, src in crs:
            adj[src].append(dst)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [0] * numCourses

        def dfs(node):
            if states[node] == 1: return True
            if states[node] == 2: return False

            states[node] = 1

            for nei in adj[node]:
                if dfs(nei):
                    return True

            states[node] = 2
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True
        