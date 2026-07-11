class Solution {
public:
    bool isPalindrome(string s) {
        auto alnum = [](char c) {
            return std::isalnum(static_cast<unsigned char>(c)) != 0;
        };


        int l = 0, r = s.size() - 1;

        while (l < r ) {
            if (!alnum(s[l])) {
                l++;
                continue;
            }
            if (!alnum(s[r])) {
                r--;
                continue;
            }
            if(tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            l++, r--;
        }
        return true;
    }
};