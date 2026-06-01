"""
input: two strings s, t of lowercase engl chars
want: boolean representing if they are anagrams of oneanother true if yes false otherwise

edge case(s):
- upper/lower
- empty input --> yes??


exp:
1) sort both inptus and use == to check if thye are the same - sorting takes O(n log n), O(1) space
2) count the frequecies in two dicts and comapre them - O(n), O(n) for this apporach
3) we can use the ord() function to count the frequencie of each char in an  arr[0] * len(input) and check like that (simialr to dict)
    should be O(n) and t and space but ord does O(1) compute
time, space - O(n), O(n)


"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count2 = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            count2[char] = count2.get(char, 0) + 1

        return count == count2
