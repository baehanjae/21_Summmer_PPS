class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums=[1,3,4,5,10]
        # target = 0

        try:
            return numsStr.index(target) # 타겟의 위치 리턴
        except: # 타겟 값이 존재하지 않을 경우
            for i in range(len(nums)):
                print('debugging', nums[i])
                if target <= nums[i]: # 타겟보다 값이 클 결우 그 자리를 리턴
                    print('debugging', nums[i])
                    return i

            return i + 1