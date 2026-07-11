class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size(), l = 0, r = n - 1;

        while (l < r) {
            int localCount = numbers[l] + numbers[r];

            if (localCount < target) {
                l++;
            }
            else if (localCount > target) {
                r--;
            }
            else{
                return vector<int>{l + 1, r + 1};
            }

        }
        return {};
    }
};
