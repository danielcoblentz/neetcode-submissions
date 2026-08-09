#define vi vector<int>
#define pb push_back

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        if (candidates.empty()) return {};
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vi subset;
        dfs(0, 0, candidates, subset, res, target);
        return res;
    }

private:
    void dfs(int i, int currentSum, vector<int>& candidates, vi& subset, vector<vector<int>>& res, int target) {
        if (currentSum == target) {
            res.pb(subset);
            return;
        }
        if (i >= candidates.size() || currentSum > target) {
            return;
        }

        // take nums[i]
        subset.pb(candidates[i]);
        dfs(i + 1, currentSum + candidates[i], candidates, subset, res, target);
        subset.pop_back();

        // skip nums[i] and dups!
        while (i + 1 < candidates.size() && candidates[i] == candidates[i + 1]) {
            i++;
        }
        dfs(i + 1, currentSum, candidates, subset, res, target);
    }
};