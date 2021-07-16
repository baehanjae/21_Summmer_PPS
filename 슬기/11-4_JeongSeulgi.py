'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort() #순서대로 정렬 
        for i in range(len(nums)-1, 1, -1): #nums[i-2], nums[i-1], nums[i] 를 뽑아내기 위해 
            if nums[i-2] + nums[i-1]  > nums[i]: #가장 큰 변의 길이가 나머지 두변의 길이의 합보다 작으면  
                return nums[i-2] + nums[i-1] + nums[i] #삼각형이 만들어지므로 둘레를 리턴 
        return 0 #그렇지 않으면 0을 리턴 
'''

'''
11-4 Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/
'''