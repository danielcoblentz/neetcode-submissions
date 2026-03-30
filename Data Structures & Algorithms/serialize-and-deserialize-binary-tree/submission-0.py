# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
            
        data = []
        def dfs(node):
            if not node:
                data.append("null")
                return
                
            data.append(str(node.val))
            left = dfs(node.left)
            right = dfs(node.right)
        dfs(root)
        separator = ","
        my_string = separator.join(data)
        print(my_string)
        return my_string
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        res = iter(data.split(","))
       # [1,2,3,null,null,4,5]
        def dfs():
            v = next(res)
            if v == "null":
                return None

            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

