# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        queue = deque([root])
        ans = []

        while queue:
            current_length = len(queue)
            rightmost_val = None

            for _ in range(current_length):
                node = queue.popleft()
                rightmost_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(rightmost_val)
        return ans