class Solution {
public:
    bool isAnagram(string s, string t) {
       unordered_map<char, int> count1;
       unordered_map<char, int> count2;

       //edge case(s)
       if (s.length() != t.length()) return false;

       for (auto& c : s) {
        count1[c]++;
       }

       for (auto& c : t) {
        count2[c]++;
       }

       return count1 == count2;
    }
};