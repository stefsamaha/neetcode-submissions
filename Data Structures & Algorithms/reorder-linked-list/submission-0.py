# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first the middle 
        slow, fast = head, head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next 
            fast = fast.next.next 
        
        # separate the halves
        second = slow.next  
        slow.next = None 

        # reverse the second half 
        previous = None 

        while second is not None:
            next_node = second.next
            second.next = previous
            previous = second
            second = next_node 
        
        # merge the two halves 
        first = head 
        second = previous 
    
        while second is not None:
            first_next = first.next
            second_next = second.next

            first.next = second 
            second.next = first_next

            first = first_next 
            second = second_next











        