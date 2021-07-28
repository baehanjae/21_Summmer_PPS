#추가 공간을 만들지 않고
#O(n) 시간 안에 수행해야  

class Solution:
    def findDisappearedNumbers(self, nums):
        set_result = set(range(1,len(nums)+1)) #범위에 해당하는 수를 중복 없이 담기 위해 set 사용
        set_nums = set(nums) #nums에 있는 중복된 수 제거하기 위해 set 사용 
        return list(set_result - set_nums) #차집합
                       
sol1=Solution()
print(Solution.findDisappearedNumbers(sol1,[4,3,2,7,8,2,3,1]))

sol2=Solution()
print(Solution.findDisappearedNumbers(sol2,[1,1]))

sol3=Solution()
print(Solution.findDisappearedNumbers(sol2,[1,2,2,4,5]))
