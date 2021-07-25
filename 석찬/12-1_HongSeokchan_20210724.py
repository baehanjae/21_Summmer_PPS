'''
https://leetcode.com/problems/sort-array-by-parity-ii/ 
'''
from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        
        # nums의 각 칸을 검사하여 홀수 짝수로 나누기
        for i in range(len(nums)) :
            if nums[i] % 2 == 0 :
                even.append(nums[i])
            else :
                odd.append(nums[i])
        
        i = 0
        # 홀수 짝수의 배열이 모두 끝나지 않았을 땐 번갈아가면서 ans 배열에 넣음
        while i < len(even) and i < len(odd) :
            ans.append(even[i])
            ans.append(odd[i])
            i += 1
        # 짝수 배열이 끝나면 홀수만 ans에 넣음
        while i < len(even) :
            ans.append(even[i])
            i+=1
        # 홀수 배열이 끝나면 짝수만 ans에 넣음
        while i < len(odd) :
            ans.append(odd[i])
            i+=1
        return ans

a = Solution()
nums = [2,3]
print(a.sortArrayByParityII(nums))