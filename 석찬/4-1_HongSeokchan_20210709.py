'''
https://www.acmicpc.net/problem/2953 
'''
result = [0,0]
max = 0

for i in range (5) :
    person = sum([int(x) for x in input().split()]) #1) input값을 ' '기준으로 파싱하여와서 2)각 하나하나의 문자를 정수형으로 바꾼 뒤 3)해당 list의 합계값을 구함
    if max <= person :
        max = person # 앞에서 구한 합계 값이 max값보다 크거나 같으면 해당 합계 값이 max
        result = [i+1,person] #현재 사람의 index+1(몇 번째 사람인지)와 합계 값을 list에 저장

print("%d %d"%(result[0],result[1])) #list에서 가져와서 출력
