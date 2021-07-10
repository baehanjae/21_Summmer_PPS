'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2: #둘다 존재하면 
            node = TreeNode(root1.val + root2.val) #값을 더하기 
            node.left = self.mergeTrees(root1.left, root2.left) #왼쪽 순회
            node.right = self.mergeTrees(root1.right, root2.right) #오른쪽 순회
            return node 
        else: 
            return root1 or root2
'''

'''
9-4 Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
'''