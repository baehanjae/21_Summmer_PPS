'''
https://leetcode.com/problems/island-perimeter/
'''
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)) :
            for j in range(len(grid[i])) : # list의 모든 칸을 한 칸 한 칸 검사
                if grid[i][j] == 1 : # 현재 검사한 칸이 1일 때 (땅 이라는 뜻)
                    # 해당 항의 상하좌우 칸을 검사하여 해당 상하좌우 칸이 0이거나 out of range 이면 해당 면이 땅의 외곽선 이므로 ans에 1을 더한다
                    if i-1 < 0 or grid[i-1][j] == 0 : ans += 1
                    if j-1 < 0 or grid[i][j-1] == 0 : ans += 1
                    if j+1 >= len(grid[i]) or grid[i][j+1] == 0 : ans += 1
                    if i+1 >= len(grid) or grid[i+1][j] == 0 : ans+=1
        return ans

a = Solution()
grid = [[1,0]]
print(a.islandPerimeter(grid))