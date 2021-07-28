class Solution:
    def missingNumber(self, nums) :
        set_result = set(range(0,len(nums)+1)) #범위에 해당하는 수를 중복 없이 담기 위해 set 사용
        set_nums = set(nums) #nums  집합으로 만들기 위해 set 사용
        return list(set_result - set_nums)[0]

sol1=Solution()
print(Solution.missingNumber(sol1,[3,0,1])) 
