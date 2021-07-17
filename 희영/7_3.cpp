class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        keys = set(nums) // 중복된 값 제거
        answer = 0
        
        // 해당 key 값이 nums의 절반 보다 많을 경우 answer값에 key 값을 저장하고 break
        for key in keys:
            if nums.count(key) > len(nums) / 2:
                answer = key
                break
        return answer