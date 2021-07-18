n= int(input())
numbers = list(set(map(int, input().split(' ')))) # 숫자들을 공백으로 구분해 입력
numbers.sort() # 오름차순으로 정렬
numbers = list(map(str, numbers)) # 리스트 변수 숫자들을 문자열로 저장
print(' '.join(numbers)) # 숫자들 공백으로 구분해 출력
