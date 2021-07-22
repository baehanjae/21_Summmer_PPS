#include <iostream>
using namespace std;

//Data structure to store a binary tree node
struct TreeNode{
    int val;
    TreeNode *left, *right;

    TreeNode(int val){
        this->val=val;
        this->left=this->right=nullptr;
    }
};

//A structure to store a node's level and parent information
struct NodeInfo{
    int key;
    int level;
    TreeNode *parent;
};

// Perform inorder traversal on a given binary tree and update `x` and `y`
void inorder(TreeNode* root, TreeNode* parent, int level, NodeInfo &x, NodeInfo &y){
    //base case: tree is empty
    if(root==nullptr)
        return;
    
    //traverse left subtree
    inorder(root->left, root, level+1, x, y);

    // if the first element is found, save its level and parent node
    if(root->val==x.key){
        x.level=level;
        x.parent=parent;
    }

    // if the second element is found, save its level and parent node
    if (root->val == y.key)
    {
        y.level = level;
        y.parent = parent;
    }

    //traverse right subtree
    inorder(root->right,root,level+1,x,y);
}


// Function to determine if two given nodes are cousins of each other
bool isCousins(TreeNode* root, int elem1, int elem2){
    //return if the tree is empty
    if(root == nullptr)
        return false;
    
    int level=1; // level of the root is 1
    TreeNode *parent = nullptr; //parent of the root is null

    NodeInfo x ={elem1,level,parent};
    NodeInfo y ={elem2,level,parent};

    // Perform inorder traversal to update information about level and parent of the two elements
    inorder(root, nullptr, 1, x, y);

    // return false if `x` and `y` have a different level or same parent
    if(x.level != y.level || x.parent == y.parent)
        return false;
    return true;
}

int main(){
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left= new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);

    if(isCousins(root,5,6)){
        cout<<"The given nodes are cousins";
    }
    else{
        cout<<"The given nodes are not cousins";
    }
}

//출처: https://www.techiedelight.com/determine-two-nodes-are-cousins/