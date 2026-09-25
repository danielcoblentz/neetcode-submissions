/*


notes:
minheap to store the (time, )

*/

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minH;
        unordered_map<int, vector<pair<int, int>>> adj;

        for (auto& t : times) {
            adj[t[0]].emplace_back(t[1], t[2]);
        }
        minH.push({0, k});
        set<int>seen;

        int t = 0;
        while (!minH.empty()) {
            auto curr = minH.top();
            minH.pop();
            int w1 = curr.first, n1 = curr.second;
            if (seen.count(n1)) continue;

            seen.insert(n1);
            t = w1;

            if (adj.count(n1)) {
                for (const auto& nxt : adj[n1]) {
                    int n2 = nxt.first, w2 = nxt.second;
                    if (!seen.count(n2)) minH.push({w1 + w2, n2});
                }
            }

        }   
        return seen.size() == n ? t : -1;
     
    }
};
