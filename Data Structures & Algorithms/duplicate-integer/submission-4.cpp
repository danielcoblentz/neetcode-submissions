/*
in: array of ints 
out: boolean, if dups present return true otherwise return false
edge case: empty array in input

time, space - 

solultion
we add all the elements to a set then if the length of the nums array does not match the length of the set then we have duplicates present so we return true
otherwise false


*/



class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
       if (nums.empty()) return false;

       unordered_set<int> seen (nums.begin(), nums.end());
       return nums.size() != seen.size();
    }
};