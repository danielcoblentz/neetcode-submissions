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
#define pb push_back
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int>res;
        if (!root) return res;
        queue<TreeNode*>q;

        q.push(root);

        while(!q.empty()) {
            int length = q.size();
            for (int i = 0; i < length; i++){
                TreeNode* node = q.front();
                q.pop();
                

                if (i == length - 1) {
                    res.pb(node->val);
                }

                if (node->left){
                    q.push(node->left);
                }
                if(node->right){
                    q.push(node->right);
                }
            }
        }
        return res;


        
    }
};