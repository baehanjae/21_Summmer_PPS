'''
https://leetcode.com/problems/same-tree/ 
inorder traversal 원리 이용하면 null이 껴있고 같은 숫자들로 이루어져 있는 tree에서는 원하는 값이 나오지 않아서
다른 방법을 생각하는데 꽤 애먹음
검색을 통해 힌트를 얻음
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q :
            return True
        elif not p or not q :
            return False
        elif p.val != q.val :
            return False
        else :
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
a = Solution()
p = [1,2,3]; q = [1,2,3]
print(a.isSameTree(p,q))
