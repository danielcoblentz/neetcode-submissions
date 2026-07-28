class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2 != 0) return false;
       unordered_map<char,char>count = {{')','('}, {']','['}, {'}','{'}};
        stack<char> st;

        for (char c : s) {
            if (count.count(c)) {
                if (!st.empty() && st.top() == count[c]) {
                    st.pop();
                }
                else {
                    return false;
                }
            }
            else{
                st.push(c);
            }
        }
        return st.empty();
    }
};