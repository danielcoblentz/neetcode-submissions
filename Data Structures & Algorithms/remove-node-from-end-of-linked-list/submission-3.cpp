/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/*
input: head of ll and an int n 
output: head of ll with nth node from end removed 
edge case: n == 0 return head, or no list return nullptr;

time, space - O(n), O(1)

notes:
get int(length) of ll in a single pass then, walk it again up to n - 1th opsition and update curr = curr.next.next
to skip the nth position in the list, and return

*/
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    if (!head) return nullptr;
       ListNode* curr = head;
       int cnt = 0;

       while (curr) {
        cnt++;
        curr=curr->next;
       } 

       if (cnt == n) {
           return head->next;
       }
//reset position
       curr = head;

       for (int i = 0; i < cnt - n - 1; i++){
        //skip position
            curr = curr->next;
       }

        curr->next = curr->next->next;
       return head;
    }
};