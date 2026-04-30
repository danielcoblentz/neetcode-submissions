class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(node):
            if node is None: return 0
            left, right = dfs(node.left), dfs(node.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        return True if dfs(root) != -1 else False