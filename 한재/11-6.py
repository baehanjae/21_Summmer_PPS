class MinStack(object):
    minstack = [] # 스택으로 사용할 리스트
    minval = 0 # 최솟값

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = [] # 객체 생성시 빈 스택을 빈 배열로 세팅

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.minstack.append(val) # 아이템 추가
        if len(self.minstack) == 1: # 최초에 push
            self.minval = val # 최소값으로 입력
        else:
            for i in self.minstack: # 이미 스택에 값이 존재하는 경우
                if i < self.minval:
                    self.minval = i # 새로운 최솟값

    def pop(self):
        """
        :rtype: None
        """
        if self.minstack[len(self.minstack) - 1] == self.minval: # 최근 값이 최소값일 경우
            self.minval = self.minstack[0] # 0번째 index값을 최소값으로 설정
            for i in self.minstack[0:len(self.minstack) - 1]: # 최근 값을 제외하고 하나씩 비교
                if i < self.minval:
                    self.minval = i
        self.minstack.pop() # 최근값 제거

    def top(self):
        """
        :rtype: int
        """
        return self.minstack[len(self.minstack) - 1] # 최근 값을 반환

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval # 최소값을 반환

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()