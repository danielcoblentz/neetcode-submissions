class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        vector<int>dp(n);

        // get start point max if idx [0,1]
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for (int i = 2; i < n; i++){
            //take prev value as hte best we cna do (skip case)
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        return dp[n - 1];
    }
};