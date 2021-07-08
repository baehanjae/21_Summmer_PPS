word = input().upper() # 입력을 전부 대문자로 변경
num = [] 

for i in range(ord('A'), ord('Z')+1): # A~Z만큼 for문을 돌리기
  num.append(word.count(chr(i))) # A~Z를 count해서 num에 append

if num.count(max(num))==1: # 가장 많은 문자가 1개 있다면 해당 알파벳 출력
  print(chr(num.index(max(num))+ord('A'))) 
else:
  print('?')

'''
2-5 단어공부
https://www.acmicpc.net/problem/1157
'''
