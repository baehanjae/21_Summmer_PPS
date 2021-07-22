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

//root node부터 시작하여 아래로 내려가면서 leaf node에 도달 할 때까지 node의 값을 이진수로 만들어 합산  
//재귀함수로 구현 (그림 그리면 이해 잘 감)
class Solution {
    public:
        int sumRootToLeaf(TreeNode* root) {
            if(root==nullptr)
                return 0;
            if(root->left==nullptr && root->right==nullptr) //leaf node이면 
                return root->val;
            if(root->left) //root의 왼쪽에 자식 노드가 존재하면 
                root->left->val += root->val*2; //왼쪽 자식 노드 값에 기존 루트의 노드 값에 *2 하여 합산
            if(root->right) //root의 오른쪽에 자식 노드가 존재하면 
                root->right->val += root->val*2; //오른쪽 자식 노드 값에 기존 루트의 노드 값에 *2 하여 합산
            return sumRootToLeaf(root->left)+sumRootToLeaf(root->right); //root의 왼쪽과 오른쪽 자식 노드가 다시 root 역할을 해나감...(계속)
        }
};