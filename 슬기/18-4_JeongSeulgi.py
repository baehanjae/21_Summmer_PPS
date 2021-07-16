'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None: #노드가 하나밖에 없으면 false
            return False
        a = list()
        while head:
            if head in a: #리스트에 있는 head를 다시 가리키면 true 
                return True
            a.append(head)
            head = head.next
        return False #그렇지 않으면 false 
'''

'''
18-4 Linked List Cycle 
https://leetcode.com/problems/linked-list-cycle/
'''