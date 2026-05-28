# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        p1, p2 = head, head

        while p1 and p1.next:
            
            p2 = p2.next
            p1 = p1.next.next

            if p1 == p2: return True
        return False