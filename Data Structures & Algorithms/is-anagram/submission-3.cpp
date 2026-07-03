class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        for (int i = 0; i < s.size(); i++) {
            sMap[s[i]]++;
        }

        for (int j = 0; j < t.size(); j++){
            tMap[t[j]]++;
        }


        for (auto& [key, val] : sMap) {
            cout << key << ":" << val << endl;

        return sMap == tMap;
    }
};
};
