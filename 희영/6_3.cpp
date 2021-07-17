class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__push_stack=[]
        self.__pop_stack=[]
        

    def push(self, x: int) -> None: // push_stack에 담는다.
        """
        Push element x to the back of queue.
        """
        self.__push_stack.append(x)


    // pop과 peek의 경우 push_stack에 있는 데이터를 
    // pop_stack에 옮겨서 순서를 바꾼 후, pop을 한다.
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.__pop_stack:
            return self.__pop_stack.pop()
        else:
            while self.__push_stack: // Push_stack을 pop_stack 으로 이동
                temp=self.__push_stack.pop()
                self.__pop_stack.append(temp)
            return self.__pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.__pop_stack:
            return self.__pop_stack[-1]
        else:
            while self.__push_stack: // Push_stack을 pop_stack 으로 이동
                temp=self.__push_stack.pop()
                self.__pop_stack.append(temp)
            return self.__pop_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.__push_stack or self.__pop_stack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()