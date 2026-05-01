# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
LCA can be found using prev whihc represents the root of hte root of hte current subtree
- we search for hte p, q nodes and see if the rootitself is (p,q) and htey must be in hte same subtree (or tree overall)
- using dfs we search for both values then we keep track of the one above it (what if the parent is p or q) is that valid


- once we know p,q are in hte same subtree and the distance is one we can return the parent we are looking at 



'''

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right # because the values must be in the right side of tree
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root # this represents the split point
