/*
input: vector of ints where each elem represents a height of a single bar
want: the max area we can hold water in
edge case: empty height array then we return 0 | are we guarenteed an input >= 2?
time, space: O(n), O(1), where n is the length of the input vector 

ans:
check edge cases

high level design
init: l,r, ans
use two poitners one at each end of the array. we iterate through the values computing a localArea which represents the current area we compute for heights[l] and height[r]
every time we compute that value we passs it into a max function so we always take the maxiumm of (ans, localArea) ans wil lrepresents the vlaue we are returning when this is done
the nwe move our poitners inwards until they meet in which we terminate the loop and return the 'ans'
*/






class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1, ans = 0;

        while (l < r) {
            int area = min(heights[l], heights[r]) * (r - l);
            ans = max(ans, area);
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return ans;
    }
};
