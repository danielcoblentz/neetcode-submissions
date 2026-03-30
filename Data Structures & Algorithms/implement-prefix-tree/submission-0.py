class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends_with = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.ends_with = True # end of word 

    def search(self, word: str) -> bool:
        # searching entire word
        curr = self.root
        for c in word:
            if c not in curr.children: # not in prefix tree
                return False
            curr = curr.children[c] # move down the level
        return curr.ends_with
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]
        return True
        
        