/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#define pd push_back
class Solution {
public:
    vector<int> res; 
    void dfs(TreeNode* node) {
        if (!node) return;
        // left, node, right --> returns sorted  order 
        dfs(node->left);
        res.pd(node->val);
        dfs(node->right);
    }

    int kthSmallest(TreeNode* root, int k) {
        if (!root) return 0;
        dfs(root);
        return res[k - 1];
    }
};