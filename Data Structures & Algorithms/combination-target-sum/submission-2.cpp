#define ll long long
#define vi vector<int>

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        if (nums.empty()) return {};
        vi subset;
        vector<vector<int>> res;
        dfs(0, 0, res, subset, nums, target);
        return res;
    }

private:
void dfs(int i, int currentSum, vector<vector<int>>& res, vi& subset, vi& nums, int target){
    if (currentSum == target) {
        res.push_back(subset);
        return;
    }
    if (i >= nums.size() || currentSum > target){
        return;
    }

    // take nums[i]
    subset.push_back(nums[i]);
    dfs(i, currentSum + nums[i], res, subset, nums, target);
    subset.pop_back();

    // skip nums[i]
    dfs(i + 1, currentSum, res, subset, nums, target);
}
};