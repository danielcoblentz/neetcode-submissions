/*
input: string of all lowercase alnum chars
want: int representing the length of the lnogest non repeating chars
ec(s): empty input, non lowercase or numbers present, always in this formt / representation?

time, space - O(n), O(n) where n is the length of the input

solution:
init a set whihc will contain each individual non repeating char form the string 's' then two poiners l and r
r will move through hte input adding chars that are not present in hte set, if thye are present we remove the char at the l index and increment l
at each time of insertion we compute the length of hte current window and comapre that to hte max length we alreayd found previosuly

when r reaches the end of the 's' then we are done and we return the answer 'res'

*/



class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       int l = 0;
       int res = 0;
       unordered_set<char> seen;

       for (int r = 0; r < s.size(); r++) {
            while (seen.contains(s[r])){
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[r]);
            //get length and comapre
            int window = (r - l + 1);
            res = max(res, window);

       } 
       return res;
    }
};
