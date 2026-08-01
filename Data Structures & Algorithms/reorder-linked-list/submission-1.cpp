class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;
        ListNode* slow = head, *fast = head->next;

        // find middle of list to parition it
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;

        //revrese the list
        while (second){
            ListNode* tmp = second->next;
            second->next = prev;
            prev = second;
            second = tmp;
        }

        ///merge
        second = prev;
        ListNode* first = head;

        while (second){
            ListNode* tmp1 = first->next, *tmp2 = second->next;
            first->next = second;
            second->next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
};