class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        char_map = {
            '2' : ["a", "b", "c"],
            '3' : ["d", "e", "f"],
            '4' : ["g", "h", "i"],
            '5' : ["j", "k", "l"],
            '6' : ["m", "n", "o"],
            '7' : ["p", "q", "r", "s"],
            '8' : ["t", "u", "v"],
            '9' : ["w", "x", "y", "z"]
        }
        # get all possible letters from our digit combination
        possible_vals, res = [], []
        for d in digits:
            possible_vals.append(char_map[d])


        def solve(index, path):
            if index == len(possible_vals) or index == len(digits):
                res.append(path[::])
                return

            for c in char_map[digits[index]]:
                solve(index + 1, path + c)


        solve(0, "")
        return res
