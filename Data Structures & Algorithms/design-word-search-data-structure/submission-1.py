class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends_with = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()   # FIX: use TrieNode, not TreeNode

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.ends_with = True     # FIX: only mark END OF WORD after inserting all chars


    def search(self, word: str) -> bool:

        def dfs(i, node):  # i = index in word
            if i == len(word):
                return node.ends_with

            c = word[i]

            # CASE 1: wildcard '.'
            if c == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            # CASE 2: normal character
            if c not in node.children:
                return False

            return dfs(i + 1, node.children[c])

        return dfs(0, self.root)