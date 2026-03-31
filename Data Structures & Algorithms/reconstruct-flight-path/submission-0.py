'''
input: 2D list of tickets where each element is [src, dst]
output: single list of all the flight paths

time, space - 

exp:
questions:
- do we need ot make hte src, dst nodes? and connect them?
- we know we are guarentted an ordering do we dont need ot worry abt empty edge case
- we need the itinerary in sorted order (lexigraphical)
- how ot amke sure we visit every place once and maintain the smallest order?


sol:
we use dfs or topological sort? to amke sure we visit each node once


'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]
