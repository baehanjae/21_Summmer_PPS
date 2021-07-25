class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums1)):
            flag = 1
            for j in range(nums2.index(nums1[i])+1,len(nums2)):
                if nums1[i] < nums2[j]:
                    res.append(nums2[j])
                    flag = 0
                    break
            if flag == 1:
                res.append(-1)
        return res
