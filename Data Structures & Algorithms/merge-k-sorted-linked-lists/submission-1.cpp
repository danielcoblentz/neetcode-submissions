class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        if (n <= 0) return nullptr;
        
        while (lists.size() > 1) {
            vector<ListNode*> res;
            for (int i = 0; i < lists.size(); i += 2){
                ListNode* l1 = lists[i];
                ListNode* l2 = (i + 1 < lists.size()) ? lists[i + 1] : nullptr;
                res.push_back(merge(l1, l2));
            }
            lists = res;
        }
        return lists[0];
    }

    ListNode* merge(ListNode* l1, ListNode* l2){
        ListNode dummy(0);
        ListNode* node = &dummy;
        while (l1 && l2){
            if (l1->val < l2->val){
                node->next = l1;
                l1 = l1->next;
            } else {
                node->next = l2;
                l2 = l2->next;
            }
            node = node->next;
        }
        if(l1) node->next = l1;
        else node->next = l2;
        return dummy.next;
    }
};