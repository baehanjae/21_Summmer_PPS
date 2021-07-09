'''
https://www.acmicpc.net/problem/2163
'''
# 접근 : 초콜릿 자르기의 최소 횟수는 두 입력값의 곱 - 1이라고 생각됨

a,b = [int(x) for x in input().split()] #1) input값을 ' '기준으로 파싱하여와서 2)각 하나하나의 문자를 정수형으로 바꾼 뒤 3)각각 ab변수에 할당
print(a*b-1)
