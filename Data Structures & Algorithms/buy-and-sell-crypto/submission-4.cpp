class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int l = 0, r = 1;

        while (r < prices.size()){
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                ans = max(ans, profit);
            }
            //if a smaller value exists then we move the pointers there
            else{
                l = r;
            }
            r++;
        }
        return ans;
    }
};
