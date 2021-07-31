'''
https://leetcode.com/problems/maximum-subarray/submissions/ 
Brute Force(하드코딩)으로 풀다가 Time Limit Exceeded 에러를 해결하지 못 함
Dynamic Programming의 개념을 처음 적용해봄
'''
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]

        # Dynamic Programing 개념 적용 (참고 : https://sustainable-dev.tistory.com/23)
        for num in nums[1:] :
            current_subarray = max(num, current_subarray+num)
            max_subarray = max(current_subarray, max_subarray)
        
        return max_subarray

a = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(a.maxSubArray(nums))