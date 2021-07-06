import copy

scale = input().split() #8개의 숫자를 입력 받음
scale2 = copy.deepcopy(sorted(scale)) #비교를 위해, 입력받은 8개의 숫자를 sorting한 후 deepcopy한 변수를 하나 더 만듦

if scale == scale2 : print("ascending") #입력 받은 숫자와 그 숫자의 sorting version이 같다면 ascending
elif scale == list(reversed(scale2)) : print("descending") #입력 받은 숫자와 그 숫자의 sorting version의 reverse가 같다면 ascending
else : print("mixed") # 둘 다 아니면 mixed

