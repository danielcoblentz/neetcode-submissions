class Solution {
public:
    int solve(vector<int>& nums, int lo, int hi) {
        int len = hi - lo + 1;
        if (len == 1) return nums[lo];

        vector<int> dp(len);
        dp[0] = nums[lo];
        dp[1] = max(nums[lo], nums[lo + 1]);

        for (int i = 2; i < len; i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[lo + i]);
        }
        return dp[len - 1];
    }

    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        return max(solve(nums, 0, n - 2), solve(nums, 1, n - 1));
    }
};