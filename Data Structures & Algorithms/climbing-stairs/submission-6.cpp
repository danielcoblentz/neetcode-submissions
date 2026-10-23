class Solution {
   public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int ob = 2, tb = 1, ans;
        for (int i = 2; i < n; i++) {
            ans = ob + tb;
            tb = ob;
            ob = ans;
        }
        return ans;
    }
};
