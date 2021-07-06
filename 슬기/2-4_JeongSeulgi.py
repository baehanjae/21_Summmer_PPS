dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

a = input() 

time=0
for i in range (len(a)):
    for j in dial:
        if a[i] in j:
            time+=dial.index(j)+3 #1이 2초, 그 다음 부터 1초씩 증가, ABC는 2이므로 +3

print(time)

'''
2-4 다이얼
https://www.acmicpc.net/problem/5622
'''