# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev, cur = None, start
            while cur != end:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        prevGroup = dummy = ListNode(0, head)

        while True:
            kth = self.getkth(prevGroup, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            start = prevGroup.next
            new_head = reverse(start, group_next)

            # reconnect links
            prevGroup.next = new_head
            start.next = group_next
            prevGroup = start
        return dummy.next



    def getkth(self,node,k):
        while node and k > 0:
            node =node.next
            k -= 1
        return node
