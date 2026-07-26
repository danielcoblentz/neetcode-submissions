class Solution {
public:

    string encode(vector<string>& strs) {
        string s;
        for (auto& str : strs){
                s += to_string(str.size()) + '#' + str;
        }

        return s;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            res.push_back(s.substr(j + 1, length));
            i = j + 1 + length;
        }
        return res;
    }
};