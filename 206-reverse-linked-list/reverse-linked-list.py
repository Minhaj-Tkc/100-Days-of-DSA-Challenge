# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        print(head)

        while curr:
            next_node = curr.next   # store next node - 2 - 3 - 4 -
            # print(next_node)
            curr.next = prev        # reverse pointer - none - 1 - 2 - 
            prev = curr             # move prev forward - 1 - 2 - 3 - 
            curr = next_node        # move curr forward - 2 - 3 

        return prev