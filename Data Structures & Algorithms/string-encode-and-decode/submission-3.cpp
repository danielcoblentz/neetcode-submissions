class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for (auto& s : strs) {
            result += to_string(s.length()) + "#" + s;
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.size()) {
            int j = s.find('#', i);
            int len = stoi(s.substr(i, j - i));
            res.push_back(s.substr(j + 1, len));
            i = j + 1 + len;
        }
        return res;
    }
};