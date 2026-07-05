/*
input: string s 
want: int representing the longest substring of the input w/o dups
edge case: empty input, non engl chars , no nums, !alnums
time, space - O(n), O(n)

*/



class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) {return 0;} // does thsi work?

        set<char> seen;
        int ans = 0;
        int n = s.size();
        int l = 0;

        for (int i = 0; i < n; i++ ) {
            //if dups remove the emtry 
            while (seen.contains(s[i])) {
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[i]);
            ans = max(ans, (int)seen.size());
        }
        return ans;


    }
};