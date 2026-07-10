class Solution {
public:
    bool is_alphanumeric(char c) {
        return std::isalnum(static_cast<unsigned char>(c)) != 0;
    }

    bool isPalindrome(string s) {
       int l = 0, r = s.size() - 1;

       while (l < r) {
        if (!is_alphanumeric(s[l])){
            l++;
        }

        else if (!is_alphanumeric(s[r])) {
            r--;
        }

        else {
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            l++, r--;
        }

       }
       return true;

    }
};
