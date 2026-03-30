class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(word) -> bool:
            l, r = 0, len(word) - 1

            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def solve(index, path):
            if index == len(s):
                res.append(path[::])
                return


            for i in range(index, len(s)):
                substring = s[index: i + 1]

                if is_palindrome(substring):
                    path.append(substring)
                    solve(i + 1, path)
                    path.pop()


        solve(0, [])
        return res
