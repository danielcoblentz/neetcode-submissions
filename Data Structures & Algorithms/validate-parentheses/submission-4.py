'''
input: string of chars
want: boolean representing if all pairs have a corresponding opening and closing pair

edge cases: only brackets right? no other chars, empty input

time, space - 

exp:

s = |    ([{}])    |
pairs = {')' : '('}

for each value we add closing brackets to the stack and if we see an opening we pop it and return of the len(stack) == 0

if its an opening bracket and hte last element on hte stack does match (corresponds pairs[s[i]]) then we pop if not we append it













'''
class Solution:
    def isValid(self, s_str: str) -> bool:
        stack = []
        pairs = {')': '(', ']':'[', '}':'{'}

        if len(s_str) % 2 != 0: return False # odd len will never be true


        for char in s_str:
            if char in pairs and stack and stack[-1] == pairs[char]: stack.pop()
            else:
                stack.append(char)
        return True if len(stack) == 0 else False