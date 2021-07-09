'''
def solution(num):
    cnt = 0
    
    while num != 1 : #숫자가 1이 되기 전까지 
        if cnt == 500 : #500번을 넘기면 -1 리턴 
            return -1 
        
        if num % 2 == 0 : #
            num = num // 2 
            
        else :
            num = num * 3 + 1
        cnt += 1 
        
    return cnt
'''

'''
10-4 콜라츠 추측 
https://programmers.co.kr/learn/courses/30/lessons/12943
'''