# Definition for singly-linked list.
// 주어진 링크드 리스트를 하나씩 새로운 링크드 리스트에 연결시켜서 반환하면 된다.
class ListNode:
    val = 0
    next = None

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        now = head
        temp = None

        while now:
            nx, now.next = now.next, temp
            temp, now = now, nx

        return temp
    
                    