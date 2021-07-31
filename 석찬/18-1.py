'''
https://leetcode.com/problems/maximum-subarray/submissions/ 
'''
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # x의 이진수 구하는 법 : 숫자 x를 2로 나눠가며 그 나머지를 기록, 마지막은 마지막 남은 x를 그대로 활용
        ans = []
        for x in range(n+1) :
            nbin = [] # 이진수를 변환한 값을 배열 형태로 저장 (x가 0~n로 변할 때 새로 할당)
            while x > 1:
                nbin.append(x%2)
                x = x//2
            nbin.append(x)
            ans.append(nbin.count(1)) #구한 이진수에서 1의 갯수를 세어 ans 배열에 저장
        return ans