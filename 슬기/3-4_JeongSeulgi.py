'''
연속 2번 같은 방법 X 
2의 배수 같은 방법 2 4 6 8 10 12 ... 
3의 배수 같은 방법 3 6 9 12 15.. 
-> 6에서 문제가 발생, 6부터는 무조건 못 연다
'''

n = int(input()) #문의 개수
a = int(input()) #첫번째 문을 여는 방법
if n>=6 :
    print("Love is open door")
else: 
    for i in range(n-1):
        a = int(not a) #0,1이 반대로 출력되도록
        print(a)

'''
3-4 문문문 
https://www.acmicpc.net/problem/17210
'''