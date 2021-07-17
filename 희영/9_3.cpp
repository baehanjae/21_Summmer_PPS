# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkdepth(self, root: TreeNode) -> bool:
    // 트리의 왼쪽 오른쪽을 돌면서 차이가 1이상 나는 지 확인
    // 1이상 차이가 날 경우 False, 아닌 경우에는 True를 리턴
        if root:
            left = self.checkdepth(root.left)
            if left == -1:
                return -1
            right = self.checkdepth(root.right)
            if right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            return max(left, right) +1
        else:
            return 0
        return count

    def isBalanced(self, root: TreeNode) -> bool:
        res = self.checkdepth(root)
        return False if res == -1 else True
        