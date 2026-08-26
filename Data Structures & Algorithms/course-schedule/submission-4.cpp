class Solution {
public:


    bool dfs(int node, unordered_map<int, vector<int>>& adj, vector<int>& states){
        if (states[node] == 1) return false;
        if (states[node] == 2) return true;

        states[node] = 1;
        for (auto& nei : adj[node]){
            if (!dfs(nei, adj, states)) return false;
        }

        states[node] = 2;
        return true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites){
    
    int n = numCourses;
    unordered_map<int, vector<int>>adj;
    vector<int> states(n, 0);

    //load map
    for (auto& p : prerequisites){
        adj[p[1]].push_back(p[0]);
    }

    for (int i = 0; i < n; i++){
        if (!dfs(i, adj, states)) return false;
    }
    return true;






        
    }
};
