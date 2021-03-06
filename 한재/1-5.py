class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1] += 1
        for i in range(len(digits)-1,-1,-1): # 햇갈렸던 거  : 리버스로 반복문 실행시키는 거에서 오래 걸렸다.
            if digits[i] == 10: # 9에서 10이 된 경우 carry가 생겨서 이를 처리해줘야 한다.
                digits[i] = 0
                if i == 0: # 10으로 바뀐 수 앞에 digit이 존재하지 않을 경우
                    digits.insert(0,1) # 제일 앞자 추가, 처음에는 append를 사용하려고 하였다가 뒤로 들어가느 것을 확인하고 변경
                else : 
                    digits[i-1] += 1 
                    
        return digits
    
'''
햇갈렸던 것 : 
1. 10이 되어서 올라가는 경우가 모든 자리에서 일어난다는 것을 감안하지 못함 -> for 문으로 해결
2. 리버스로 반복문 실행시키는 문법
3. 앞에서 숫자 넣는 문법이 기억이 안남 -> insert(index,value)
*첫날은 6번으로 배정으 받지 않아서 5번을 풀음
'''
