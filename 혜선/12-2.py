class Solution:
    def merge(self, nums1, m, nums2, n) :
        del nums1[m:] #nums1의 m번째 인덱스 원소부터 끝까지 삭제
        for i in range(len(nums2)) : #nums2 원소를 nums1에 추가
            nums1.append(nums2[i]) 
        nums1.sort() #nums1을 ascending sort하기
        return nums1 
        


sol1=Solution
print(Solution.merge(sol1,[1,2,3,0,0,0],3,[2,5,6],3))


sol3=Solution
print(Solution.merge(sol3,[1,2,3,4,0,0,0,0],4,[1,4,5,7],4))

sol4=Solution
print(Solution.merge(sol4,[0],0,[1],1))
