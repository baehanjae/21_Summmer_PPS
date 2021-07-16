'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
class Solution:
    min_value = sys.maxsize #min 값을 구하기 위해 최대값으로 
    prev = None #루트 처리를 위해 None으로 
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left: #inorder 순회를 위해 
            self.minDiffInBST(root.left)
            
        if self.prev != None:
            self.min_value = min(self.min_value, root.val - self.prev) #현재 노드의 값과 이전 노드의 값의 차의 최솟값을 구하기 위한 코드 
       
        self.prev = root.val #처음에는 root값을 넣어준다
        
        if root.right: #inorder 순회를 위해 
            self.minDiffInBST(root.right)
        
        return self.min_value
'''

'''
14-4 Minimum Distance Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''