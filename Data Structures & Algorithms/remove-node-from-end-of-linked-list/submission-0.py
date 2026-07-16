# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        i = dummy
        j = dummy


        for x in range(n+1):
            i = i.next 

        while i is not None:
            i = i.next
            j = j.next

        
        j.next = j.next.next 
    
        return dummy.next

        