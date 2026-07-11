class Solution {
public:
    int maxArea(vector<int>& heights) {
        if (heights.size() == 0) {return 0;}
        int ans = 0, n = heights.size(), l = 0, r = n - 1;

        while (l < r ){ 
            int area = min(heights[l], heights[r]) * (r - l);
            ans = max(ans, area);
            if (heights[l] > heights[r]) {
                r--;
            } 
            else {
                l++;
            }
        }
        return ans;
    }
};
