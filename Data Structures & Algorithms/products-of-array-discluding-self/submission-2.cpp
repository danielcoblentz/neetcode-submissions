class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>res;
        vector<int>preF(n + 1, 1);
        vector<int>postF(n + 1, 1);

        // populate pre & psot fix arrays

        for (int i = 0; i < n; i++) {
            preF[i + 1] = preF[i] * nums[i];
        }

        for (int i = n - 1; i >= 0; i--) {
            postF[i] = postF[i + 1] * nums[i];
        }

        for (int i = 0; i < n; i++) {
            res.push_back(preF[i] * postF[i + 1]);
        }
        return res;
    }
};
