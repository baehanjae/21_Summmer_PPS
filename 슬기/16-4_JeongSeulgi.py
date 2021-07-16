'''
def solution(n):
    if n < 2 : 
        return 1 #n이 1일 때는 1 
    a, b = 1, 2 #n이 1일 때는 1, n이 2 일 때는 2 
    for i in range (2, n):
        a, b = b, a+b #직전 두개를 더하면 현재의 값 
    return b % 1234567 #문제에서 1234567로 나눈 나머지를 구하라고 했으므로
'''

'''
16-4 멀리 뛰기 
https://programmers.co.kr/learn/courses/30/lessons/12914
'''