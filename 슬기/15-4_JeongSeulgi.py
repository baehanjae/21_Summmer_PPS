'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        #'왼쪽과 오른쪽 중 더 깊은 곳 + 1' 을 반환하도록 하면 반환할 때마다 1씩 더해져서 깊이를 구할 수 있다. 
'''

'''
15-4 Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''