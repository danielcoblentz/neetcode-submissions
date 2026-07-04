class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int l = 0, r = numbers.size() - 1;
        while (l < r) {
            int localSum = numbers[l] + numbers[r];
            if (localSum == target) {
                return {l + 1, r + 1};
            }
            else if (localSum < target) {
                l ++;
            }
            else{
                r --;
            }  
        }
        return {};
    }
};