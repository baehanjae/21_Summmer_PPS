n = int(input())
a = list(str(n)) # 입력받은 n을 a리스트에 저장
a.sort() # 정렬한다
a.reverse() # 뒤집는다

for n in a:
  print(n, end="") # 출력
