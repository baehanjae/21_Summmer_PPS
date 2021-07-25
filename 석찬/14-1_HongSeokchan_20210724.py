'''
https://leetcode.com/problems/leaf-similar-trees/ 
'''
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def inorder (root : TreeNode, leaves : List) -> List[int]:
            # Binary tree Inorder traversal 원리 이용
            if not root : return

            inorder(root.left, leaves)
            if not root.left and not root.right : leaves.append(root.val) # 해당 노드의 오른쪽 하위 노드와 왼쪽 하위 노드가 없을 때 (leaf 노드 일 때) value값을 ans에 append
            inorder(root.right, leaves)
            return leaves
        
        r1Leaves = inorder(root1,[])
        r2Leaves = inorder(root2,[])
        return r1Leaves == r2Leaves

a = Solution()
root1 = [3,5,1,6,2,9,8,None,None,7,4];
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
print(a.leafSimilar(root1,root2))
