'''
https://leetcode.com/problems/sum-of-all-subset-xor-totals/ 
문제를 푸는데 어려움을 느껴 구글링에 도움을 받음
'''
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:        
        subsets = []
        
        self.find_subsets(nums, 0, [], subsets)
        
        results = 0
        
        for subset in subsets:
            if not subset:
                results += 0
            
            else:
                xor_total = reduce(lambda x, y: x ^ y, subset)
                results += xor_total
        
        return results
        
        
    def find_subsets(self, nums, start, combination, results):        
        results.append(list(combination)) #이전에 계산되어 parameter로 전달된 조합들을 result에 append
        
        for i in range(start, len(nums)):
            num = nums[i]
            combination.append(num)
            self.find_subsets(nums, i + 1, combination, results) #시작 위치를 하나 늘려 recursion
            combination.pop()

a = Solution()
nums = [1,3]
print(a.subsetXORSum(nums))