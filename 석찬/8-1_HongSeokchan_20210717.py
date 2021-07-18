'''
https://deok2kim.tistory.com/125 
검색을 참고함
'''
def solution(cookie):
    answer = 0
    n = len(cookie) 
    for i in range(n - 1): # 형 부분과 동생 부분의 기준점 (0부터 시작해서 형과 동생이 같은 값을 받는 것을 찾을 때까지 오른쪽으로 이동)
        left_sum, left_idx = cookie[i], i # 형 과자와 그 index 초기화 
        right_sum, right_idx = cookie[i + 1], i + 1 # 동생 과자와 그 index 초기화 
        while True:
            if left_sum == right_sum: # 형 동생의 값이 같을 시
                answer = max(answer, left_sum) 
            if left_idx > 0 and left_sum <= right_sum: # 동생이 더 많을 때
                left_idx -= 1
                left_sum += cookie[left_idx]
            elif right_idx < n - 1 and right_sum <= left_sum: # 형이 더 많을 때
                right_idx += 1
                right_sum += cookie[right_idx]
            else:
                break
    return answer