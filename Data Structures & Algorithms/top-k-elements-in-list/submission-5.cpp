class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        for (int num : nums) {
            count[num]++;
        }

        priority_queue
        <pair<int,int>,
        vector<pair<int, int>>,
        greater<pair<int, int>>
        > minH;

        for (auto& entry : count) {
            minH.push({entry.second, entry.first});
            if (minH.size() > k) {
                minH.pop();
            }
        } 

        vector<int> res;
        for (int i = 0; i < k; i++){
            res.push_back(minH.top().second);
            minH.pop();
        }
        return res;
    }
};
