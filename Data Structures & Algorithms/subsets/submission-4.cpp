
#define pb push_back
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>res;
        vector<int>subset;
        dfs(0, nums, res, subset);
        return res;
        
    }


private:
void dfs(int i, vector<int>& nums, vector<vector<int>>& res, vector<int>& subset){
    if (i >= nums.size()){
        res.pb(subset);
        return;
    }

    //take nums[i]
    subset.pb(nums[i]);
    dfs(i + 1, nums, res, subset);
    subset.pop_back();

    //skip nums[i]
    dfs(i + 1, nums, res, subset);
}
};
