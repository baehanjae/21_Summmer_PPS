class Solution:
    # 재귀 호출에서 전역적으로 접근하기 위한 클래스 변수 '지름'.
    max_num = 0
    
    # 지름 탐색 재귀 호출 함수.
    def diameter(self, node):
        # 말단 노드라면 0을 반환하여 탐색 시작.
        if node is None:
            return 0
        
        # 왼쪽 서브 트리의 지름 탐색.
        left= self.diameter(node.left)
        # 오른쪽 서브 트리의 지름 탐색.
        right= self.diameter(node.right)
        # 최대 지름을 왼쪽, 오른쪽 서브 트리의 높이의 합과 비교하여 갱신.
        # 함수에서 더 큰 서브 트리의 높이를 기준으로 반환하기 때문에 가능한 것.
        self.max_num = max(self.max_num, left + right)
        
        # 서브 트리의 높이 중 더 큰 값에 1을 더해서 반환.
        # 상위 노드에서는 현재 서브 트리의 결과를 이용해서 지름을 계산해야 함.
        # 두 서브 트리 중 더 큰 쪽의 서브 트리를 이용하여 슈퍼 트리로 합치는 과정.
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 루트 노드부터 말단 노드로 탐색 시작.
        self.diameter(root)
        return self.max_num

"""
출처: https://velog.io/@park2348190/Diameter-of-Binary-Tree
"""
