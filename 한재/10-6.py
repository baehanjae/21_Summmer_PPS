class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a,2) + int(b,2),'b')

'''
format 함수를 사용하여서 수를 바이너리로 표현할 수 있다.
'''