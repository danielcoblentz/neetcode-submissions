class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seen;
        int n = nums.size();

        for (int i = 0; i < n; i++){
            if (!seen.contains(nums[i])){
                seen.insert(nums[i]);
            }

        }
        if (seen.size() != n) {
            return true;
        }
        return false;
    }
};