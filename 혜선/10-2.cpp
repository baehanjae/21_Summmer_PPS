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
class Solution {
    public:
        TreeNode* increasingBST(TreeNode* root) {
            TreeNode *dummy = new TreeNode(0);
            prev=dummy; //dummy node로 초기화 
            inorder(root);
            return dummy->right;
        }

    //left node -> root -> right node 순서로 node를 뽑아내어 구성해야 (inorder traverse를 해야!)
    private:
        TreeNode *prev;
        void inorder(TreeNode* root){
            if(root==nullptr)
                return;
            inorder(root->left);
            //node를 뽑아내어서, 오른쪽으로 쏠린 tree형태로 만들어야 
            prev->right=root; //prev의 오른쪽은 해당 node
            prev=root; //prev는 해당 node
            prev->left=nullptr; //prev의 왼쪽은 NULL
            inorder(root->right);
        }    
};

//출처: https://www.programmersought.com/article/73044934134/

