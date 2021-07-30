import bisect
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        result = set()
        # Sorting: O(n log n)
        nums2.sort()
        # Binary search for n times: O(n log n)
        for n in nums1:
            i = bisect.bisect_left(nums2,n)
            if i < len(nums2) and nums2[i] == n:
                result.add(n)

        return list(result)
