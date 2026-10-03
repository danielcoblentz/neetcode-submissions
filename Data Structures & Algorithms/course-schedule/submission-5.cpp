class Solution {
public:


    bool dfs(int node, unordered_map<int, vector<int>>& adj, vector<int>& states) {
        if (states[node] == 1) return false; // cycle
        if (states[node] == 2) return true;  // already done
        states[node] = 1;
        for (auto nxt : adj[node])
            if (!dfs(nxt, adj, states)) return false;
        states[node] = 2;
        return true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adj;

        for (const auto& crs : prerequisites) {
            int src = crs[1], dst = crs[0];
            adj[src].push_back(dst);
        }

        vector<int> states(numCourses, 0);

        for (int i = 0; i < numCourses ; i++) {
            if (!dfs(i, adj, states)) return false;
        }
        return true;
    }
};
