'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums)) #중복제거
        temp.sort()
        for i, v in enumerate(temp): #num에 중복 제거한 temp
            nums[i]=v
        return len(temp)
'''

'''
8-4 
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''