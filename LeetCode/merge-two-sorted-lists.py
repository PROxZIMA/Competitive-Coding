# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:                
        if not(A or B): return
        if not(A and B): return A or B
        
        if (A.val < B.val):
            head = A
            head.next = self.mergeTwoLists(A.next, B)
        else:
            head = B
            head.next = self.mergeTwoLists(A, B.next)
        
        return head

    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        if not (A and B):
            return A if (not B) else B

        dummy = ListNode()

        tail = dummy
        while True:
            if not(A and B):
                tail.next = A or B
                break

            if A.val <= B.val:
                tail.next = A
                A = A.next
            else:
                tail.next = B
                B = B.next

            tail = tail.next

        return dummy.next
