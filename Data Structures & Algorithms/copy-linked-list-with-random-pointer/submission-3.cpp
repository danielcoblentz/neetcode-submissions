class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* curr = head;
        unordered_map<Node*, Node*> count;

        //populate map with {old: new node}
        while (curr) {
            count[curr] = new Node(curr->val);
            curr = curr->next;
        }

        curr = head;
        while (curr){
            count[curr]->next = count[curr->next];
            count[curr]->random = count[curr->random];
            curr = curr->next;
        }
        return count[head];
    }
};