# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = ListNode(0)
        cur = temp

        while True:
            minNode = -1
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                
                if minNode == -1 or lists[i].val < lists[minNode].val:
                    minNode = i
            
            if minNode == -1: # no non-empty list found, merge is complete
                break 
            
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next 
        
        return temp.next