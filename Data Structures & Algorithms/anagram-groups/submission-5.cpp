
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //EC
        if (strs.empty()) return {};

        //init
        vector<vector<string>> res;
        map<vector<int>, vector<string>> count;

        for (auto& word : strs) {
            vector<int> tmp(26, 0);
            for (auto& c : word) {
                tmp[c - 'a']++;
            
            }
            count[tmp].push_back(word);


        }
        for (auto& [key, val]: count) {
            res.push_back(val);
        }
        return res;
    }
};
