class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<pair<int, int>>> adj;
        set<int> seen;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minH;
        int maxTime = 0;

        for (const auto& t : times) {
            int src = t[0], dst = t[1], cost = t[2];
            adj[src].emplace_back(dst, cost);
        }

        //time, starting node
        minH.push({0, k});

        while (!minH.empty()) {
            auto [time, node] = minH.top();
            minH.pop();

            if (seen.count(node)) continue;
            seen.insert(node);
            maxTime = time; // return this

            for (auto [nxtNode, edgeCost] : adj[node]) {
                if (!seen.count(nxtNode)) minH.push({time + edgeCost, nxtNode});
            }

        }
        return seen.size() == n ? maxTime : -1;  
        
    }
};
