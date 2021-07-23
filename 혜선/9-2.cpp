#include <iostream>

using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution{
    int max_num=0;
    public:
        int diameterOfBinaryTree(TreeNode* root){
            diameter(root);
            return max_num;
        }
        int diameter(TreeNode* root){
            if(root==nullptr)
                return 0;
            int left=diameter(root->left);
            int right=diameter(root->right);
            max_num=max(max_num, left+right);
            return max(left,right)+1;
        }
};
