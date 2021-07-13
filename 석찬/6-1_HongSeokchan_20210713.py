'''
https://www.acmicpc.net/problem/2164 
'''
from collections import deque

deq = deque(list(range(1, int(input())+1)))
while len(deq) > 1 : 
    deq.popleft()
    deq.append(deq.popleft())
print(deq.popleft())


'''
s = "".join([str(x) for x in range(1,int(input())+1)])
ls = len(s)
while ls > 1 : s = s[2:ls]+s[1]
print(s)
'''


