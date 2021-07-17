# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def DFS(root, targetSum, curr):
            if root:
                curr += root.val
                // 만약 트리노드의 끝이고, targetSum과 같다면
                if curr == targetSum and root.left == None and root.right == None:
                    return True
                return DFS(root.left, targetSum, curr) or DFS(root.right, targetSum, curr)
        return DFS(root, targetSum, 0)