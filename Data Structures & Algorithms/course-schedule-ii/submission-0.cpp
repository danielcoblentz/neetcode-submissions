#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // returns false if a cycle is found
    bool dfs(int node, vector<int>& states, vector<vector<int>>& adj, vector<int>& res) {
        if (states[node] == 1) return false;   // back edge -> cycle
        if (states[node] == 2) return true;    // already finished

        states[node] = 1;
        for (int nei : adj[node]) {
            if (!dfs(nei, states, adj, res)) return false;
        }
        states[node] = 2;
        res.push_back(node);
        return true;
    }

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int n = numCourses;

        // dense labels 0..n-1 -> sized vector, not a hash map
        vector<vector<int>> adj(n);
        for (auto& p : prerequisites) {
            adj[p[0]].push_back(p[1]);
        }

        vector<int> states(n, 0);
        vector<int> res;
        for (int i = 0; i < n; i++) {
            if (!dfs(i, states, adj, res)) return {};   // cycle -> impossible
        }
        return res;
    }
};
