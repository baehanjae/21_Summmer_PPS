'''
https://www.acmicpc.net/problem/10814 
'''
l = [input().split() for i in range(int(input()))]
l.sort(key = lambda x : int(x[0]))
for i in range(len(l)) :
    print(f'{l[i][0]} {l[i][1]}')