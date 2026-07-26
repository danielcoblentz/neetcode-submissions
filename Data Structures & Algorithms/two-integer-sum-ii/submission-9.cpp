/*
input: a array of ints & a int representing a target value in the array
want: a pair of idx's of two values that add to the target number

ec: empty input or target <= 0
time, space - O(n), O(1) 
solution:
init two pointers l, r at ech end of hte array then sort the input and compute a localCount whihc represnts the current sum
depepnding on the value of hte sum if less then we know we must increment l since numbers are in non decreasing order
and vice versa for the opposite case

if we find the two values we return those idx's + 1

*/


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        int count = 0;

        while (l < r) {
            count = numbers[l] + numbers[r];
            if (count < target) {
                l ++; 
            }
            else if (count > target) {
                r--;
            }
            else if (count == target) {
                return {l + 1, r + 1};
            }
            
        }
        return {};
    }
};
