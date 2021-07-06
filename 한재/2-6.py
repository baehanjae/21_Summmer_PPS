index = int(input())
sum = 0
for i in range(index):
    strList = [] # 중복되는 문자를 확인하기 위한 배열
    s = input()
    sum += 1 # 기본으로 sum 값을 늘린다.
    pre_j = '0' # 연속되는 글자들을 확인하기 위한 변수
    for j in s:
        if j in strList and pre_j != j:
            sum -= 1 # 해당 문자열이 중복이 나오면 sum 값을 원래 값으로 돌린다.
            break # continue가 아니라 break다.
        else:
            strList.append(j) # 중복이 되지 않은 문자열을 리스트에 추가
            pre_j = j # 이전 글자를 저장
print(sum) # 결과 출력

'''
*어려웠던 점
1. 연속해서 나오는 것은 넘기는 논리를 생각하기가 어려웠다.
2. 백준이 테스트 케이스에 대한 정보가 없어서 힘들었다.
'''