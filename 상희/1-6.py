n = int(input("Input: ")) # 입력 값 가져옴
a = [] 

for i in range(n): # for loop이용해서 리스트 추가
  a.append([])
  a[i].append(1)

  for j in range(1, i): # 0 ~ n-1까지 추가
    a[i].append(a[i - 1][j - 1] + a[i - 1][j])

  if (n != 0): # 하위 리스트에 1 추가
    a[i].append(1)

for i in range(n): # 파스칼 삼각형 형식으로 띄어쓰기
  print(" " * (n - i), end = " ")

  for j in range(0, i + 1): # 삼각형 내부 숫자 값
    print('{0:6}'.format(a[i][j]), end = " ")

  print()

  '''
  1-6 파스칼 삼각형
  https://leetcode.com/problems/pascals-triangle/
  '''
