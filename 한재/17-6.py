class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        k = 0 # 소팅을 위한 인덱스 변수
        so = []  # sort O
        sx = []  # sort x
        # so,sx는 arr2에 있지 않는 원소들과 있는 원소들을 구분해 없는 원소들도 소팅하는데 사용
        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]: # k 번쨰 자리에 arr2의 순서에 맞게 정렬
                    temp = arr1[k]
                    arr1[k] = arr1[j]
                    arr1[j] = temp
                    k += 1

        for s in arr1: # so,sx 생성
            if s in arr2:
                so.append(s)
            else:
                sx.append(s)

        sx.sort() # sx sorting
        res = so + sx

        return res
