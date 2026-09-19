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
 input: 2 linkedlists 
 output: one single merged linkedlist where it is in non decreasing order
 edge case(s): empty lsits either l1 or l2, odd length lists we need ot handle that
 
 time, space - 

 notes:
 make dummy node for new ll, which we will append nodes from the other 2 provided lists to, using a pointer per input lists we can check the vlas of each ie if (list1.val > list2.val) {append list1 to new list, increment ptr} kee pgoing until the two lists are empty and return dummy.next to get the head of the result.   

 
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
       ListNode dummy(0);
        ListNode* curr = &dummy;
       while (list1 && list2) {
            if (list1->val <= list2->val) {
                curr->next = list1;
                list1 = list1->next;
            } else {
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
       } 
        // odd length lists edge case
       if (list1) {
        curr->next = list1;
       }
       else{
        curr->next = list2;
       }
       return dummy.next;
    }
};
