# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = collections.deque(); #큐 선언
        q.append(root) # 루트 노드 추가
        ans = [] # 반환용 변수

        while q: # q가 null이 될떄까지 반복
            _len = len(q) # 최초 큐의 레벨의 크기 추가
            level_nodes = [] # 각 레벨의 노드를 추가할 리스트
            while _len: # 최초 입력된 큐의 길이 만큼 반복
                node = q.popleft(); # 큐에서 node 가져옴
                if node.left: #왼쪽 노드가 존재한다면 큐에 추가
                    q.append(node.left)
                if node.right: #오른쪽 노드가 존재한다면 큐에 추가
                    q.append(node.right)
                level_nodes.append(node.val) 현재 노드의 값을 레벨 노드에 추가
                _len -= 1
            ans.append(float(sum(level_nodes)) / len(level_nodes)) # 각레벨의 평균 값 계산

        return ans