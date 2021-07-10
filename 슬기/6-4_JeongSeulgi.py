'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        dq = deque() 
        
        while head != None:
            dq.append(head.val)
            head = head.next 
            
        while len(dq)>1:
            right = dq.pop()
            left = dq.popleft()
            if right != left:
                return False 
        
        return True

리트코드에서 실행되는 코드 
'''

'''
6-4 Palindrome Linked List 
https://leetcode.com/problems/palindrome-linked-list/
'''