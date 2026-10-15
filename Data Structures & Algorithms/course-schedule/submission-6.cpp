class Solution {
   public:
    bool dfs(int node, unordered_map<int, vector<int>>& adj, vector<int>& states) {
        if (states[node] == 1) return false;
        if (states[node] == 2) return true;

        states[node] = 1;
        // exp nei
        for (auto& nei : adj[node]) {
            if (!dfs(nei, adj, states)) return false;
        }

        // explored all nei and no cycles
        states[node] = 2;
        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adj;
        int n = numCourses;
        vector<int> states(n, 0); // pop the v[i] = 0 init
        for (const auto& e : prerequisites) {
            int nxt = e[0], pre = e[1];
            cout << nxt << pre << endl;
            adj[pre].push_back(nxt);
        }

        for (int i = 0; i < n; i++) {
            if (!dfs(i, adj, states)) return false;
        }

        return true;
    }
};
