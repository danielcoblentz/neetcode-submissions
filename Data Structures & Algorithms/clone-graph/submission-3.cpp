/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

input: node which contains the value and a list of nei
want:list of lists with the node values where each index position represent the node numebr and hte sublist is hte list of neighbors
edge case(s): empty input

time, space - O(v+e), O(v+e)

notes

start by making the adj mapping old to new where hte key is hte old node and hte value is hte deep copy of hte new node

we then iterate through hte neighbors of hte newnodes once copied and append the 


*/

class Solution {
public:

    Node* dfs(Node* node, map<Node*,Node*>& mp){
        if (node == nullptr) return nullptr;
        if (mp.count(node)) return mp[node]; // we previously seen this node

        Node* copy = new Node(node->val);
        mp[node] = copy;

        for(Node* nei : node->neighbors){
            copy->neighbors.push_back(dfs(nei, mp));
        }
        return copy;
    }
    Node* cloneGraph(Node* node) {
        map<Node*, Node*>mp;
        return dfs(node, mp);
        
    }
};
