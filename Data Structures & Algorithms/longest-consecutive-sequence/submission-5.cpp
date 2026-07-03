class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        int ans = 1;
        unordered_set<int> seen;

        for (int num : nums) {
            if (!seen.count(num)){
                seen.insert(num);
            }
        }

        for (int num : nums) {
            if (!seen.count(num - 1)) {
                int currentNum = num;
                int localCount = 1;
                while (seen.count(currentNum + 1)) {
                    currentNum += 1;
                    localCount += 1;
                }
                ans = max(localCount, ans);
            }
        }
        return ans;
    }
};