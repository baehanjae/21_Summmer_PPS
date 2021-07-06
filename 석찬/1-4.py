index = int(input())

for i in range(index):
    inputStr = list(map(int,input().split()))
    inputSum = 0
    inputAvg = 0
    for j in range(1,inputStr[0]+1):
        inputSum += inputStr[j]
    inputAvg = inputSum / inputStr[0]
    print(inputSum, inputStr[0])
    print(inputAvg)
        
