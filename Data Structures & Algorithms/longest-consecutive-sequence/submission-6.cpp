/*
input: list of integers 
want: the LCS of the array

edge case(s) - empty input or no seq found
time, space - O(n), O(n) where n is the size of the input

solution
convert nums to a set then init a lcs to 0, iterate through the input while the current num - 1
in seen we increment the lcs (this stars at 1) use a greedy approach to capture the overall result and hte max found os far
until we get odne iterting through the array
*/



class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        unordered_set<int> seen(nums.begin(), nums.end());
        int ans = 0;

        for (int x : seen) {
            if (!seen.contains(x - 1)) {
                int currentNum = x;
                int localCount = 1;
                while (seen.contains(currentNum + 1)) {
                    currentNum++;
                    localCount++;
                }
                ans = max(ans, localCount);
            }
        }
        return max(ans, nums.empty() ? 0 : 1);
    }
};
