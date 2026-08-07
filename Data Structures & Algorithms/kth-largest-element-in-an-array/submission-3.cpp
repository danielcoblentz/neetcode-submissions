class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int>maxH;

        for (auto& num : nums) {
            maxH.push(num);
        }

        for (int i = 0; i < k - 1; i++){
            maxH.pop();
        }
        return maxH.top();
}
};