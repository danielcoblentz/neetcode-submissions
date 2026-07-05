class Solution {
public:
    int characterReplacement(string s, int k) {
        if (s.empty()) {return 0;}
        int l = 0, ans = 0, n = s.size();


        unordered_map<char, int> count;
        
        for (int r = 0; r < n; r++){
            count[s[r]]++;

            //get max freq char in map
            auto maxIt = max_element(count.begin(), count.end(),[](auto& a, auto& b) { return a.second < b.second; });
            if ((r - l + 1) - maxIt->second <= k) {
                ans = max(ans, r - l + 1);
            }
            else{
                count[s[l]]--;
                l++;
            }
            
        }
        return ans;
    }
};