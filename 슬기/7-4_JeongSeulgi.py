s = input()
ans = list()

for i in range(len(s)):
    ans.append(s)
    s = s[1:] #s[0]만 제외하고 나머지를 s에 저장 
    
ans.sort() #알파벳 순서로 정렬 

for i in ans:
    print(i)

'''
7-4 접미사 배열 
https://www.acmicpc.net/problem/11656
'''