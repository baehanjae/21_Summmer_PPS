'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head 
        length = 0 #전체 노드의 개수를 세는 변수 
        
        while node: #노드가 존재할때까지 
            node = node.next #다음노드를 가리키도록
            length += 1 #길이를 +1 
            
        length //= 2 #절반이 몇번째인지 구하는 부분 
        
        while length > 0: #절반이 어디를 가리키는지 구하는 부분 
            head = head.next  
            length -= 1 
        
        return head       
'''

'''
12-4 Middle or the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
'''